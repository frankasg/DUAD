-- SQLite
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    code        VARCHAR(10) NOT NULL UNIQUE,
    name        VARCHAR(25) NOT NULL,
    price       DECIMAL(10, 2) NOT NULL,
    entry_date  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    brand       VARCHAR(25) NOT NULL,
    stock       INT DEFAULT 0 
);

CREATE TABLE product_invoice (
    product_invoice_id   INTEGER PRIMARY KEY,
    product_id           INT REFERENCES products(product_id),
    invoice_id           INT REFERENCES invoices(invoice_id),
    quantity             INT NOT NULL,
    total_amount         DECIMAL(10, 2) NOT NULL    
);

CREATE TABLE invoices (
    invoice_id      INTEGER PRIMARY KEY,
    invoice_number  INT NOT NULL UNIQUE,
    purchase_date   TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    buyer_email     VARCHAR(50) NOT NULL,
    total           INT DEFAULT 0
);

CREATE TABLE shopping_cart_product (
    shopping_cart_product_id   INTEGER PRIMARY KEY,
    product_id                 INT REFERENCES products(product_id),
    shopping_cart_id           INT REFERENCES shopping_carts(shopping_cart_id) 
);

CREATE TABLE shopping_carts (
    shopping_cart_id    INTEGER PRIMARY KEY,
    buyer_email         VARCHAR(50) NOT NULL
);

ALTER TABLE invoices ADD phone_number  VARCHAR(10) NULL;
ALTER TABLE invoices ADD employee_code VARCHAR(10) NULL;


---------------- INSERCIÓN DE DATOS -------------------

PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

INSERT INTO products
    (code, name, price, brand, stock)
VALUES
    ('P001', 'Teclado',    25000, 'Logitech', 30),
    ('P002', 'Mouse',      15000, 'Logitech', 50),
    ('P003', 'Monitor',   125000, 'Samsung',  15),
    ('P004', 'Laptop',    450000, 'Lenovo',    8),
    ('P005', 'Audifonos',  55000, 'Sony',     20),
    ('P006', 'Cable HDMI',  5000, 'Ugreen',   60),
    ('P007', 'Camara web', 50000, 'Logitech', 12),
    ('P008', 'Impresora',  85000, 'Epson',     0);


INSERT INTO invoices
    (invoice_number, purchase_date,
     buyer_email, phone_number, employee_code)
VALUES
    (1001, '2026-10-01 09:15:00',
     'ana@example.com', '88881111', 'EMP001'),

    (1002, '2026-10-02 10:30:00',
     'luis@example.com', '88882222', 'EMP002'),

    (1003, '2026-10-05 14:00:00',
     'ana@example.com', '88881111', 'EMP001'),

    (1004, '2026-10-10 11:45:00',
     'maria@example.com', '88883333', 'EMP002'),

    (1005, '2026-10-15 16:20:00',
     'luis@example.com', NULL, 'EMP001'),

    (1006, '2026-10-20 08:40:00',
     'ana@example.com', '88881111', NULL);


WITH details (code, invoice_number, quantity) AS (
    VALUES
        ('P001', 1001, 1),
        ('P002', 1001, 2),
        ('P003', 1002, 1),
        ('P002', 1002, 1),
        ('P001', 1003, 2),
        ('P005', 1003, 1),
        ('P004', 1004, 1),
        ('P003', 1004, 1),
        ('P002', 1005, 3),
        ('P006', 1005, 2),
        ('P005', 1006, 1),
        ('P007', 1006, 1)
)
INSERT INTO product_invoice
    (product_id, invoice_id, quantity, total_amount)
SELECT
    p.product_id,
    i.invoice_id,
    d.quantity,
    d.quantity * p.price
FROM details AS d
JOIN products AS p ON p.code = d.code
JOIN invoices AS i ON i.invoice_number = d.invoice_number;

INSERT INTO shopping_carts (buyer_email)
VALUES
    ('ana@example.com'),
    ('luis@example.com'),
    ('maria@example.com'),
    ('carlos@example.com');


WITH content (buyer_email, code) AS (
    VALUES
        ('ana@example.com',    'P003'),
        ('ana@example.com',    'P006'),
        ('luis@example.com',   'P001'),
        ('luis@example.com',   'P005'),
        ('maria@example.com',  'P007'),
        ('carlos@example.com', 'P002'),
        ('carlos@example.com', 'P004')
)
INSERT INTO shopping_cart_product
    (product_id, shopping_cart_id)
SELECT
    p.product_id,
    sc.shopping_cart_id
FROM content AS c
JOIN products AS p ON p.code = c.code
JOIN shopping_carts AS sc ON sc.buyer_email = c.buyer_email;

UPDATE invoices
SET total = (
    SELECT COALESCE(SUM(pi.total_amount), 0)
    FROM product_invoice AS pi
    WHERE pi.invoice_id = invoices.invoice_id
);

COMMIT;