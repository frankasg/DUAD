
--1
SELECT product_id,
       code,
       name,
       price,
       entry_date,
       brand,
       stock
  FROM products  

--2
SELECT product_id,
       code,
       name,
       price,
       entry_date,
       brand,
       stock
  FROM products 
 WHERE price > 50000

--3
    SELECT i.buyer_email,
        i.invoice_number,
        p.code,
        p.name,
        p.price
      FROM products p
INNER JOIN product_invoice pi
        ON p.product_id = pi.product_id
INNER JOIN invoices i
        ON pi.invoice_id = i.invoice_id
     WHERE p.product_id = 3

--4
  SELECT p.code,
       p.name,
       SUM(pi.quantity) AS unidades_compradas,
       SUM(pi.total_amount) AS monto_total
  FROM products AS p
 INNER JOIN product_invoice AS pi
    ON p.product_id = pi.product_id
 GROUP BY p.product_id

--5
    SELECT i.invoice_number,
        i.purchase_date,
        SUM(pi.total_amount) total
      FROM invoices i
INNER JOIN product_invoice pi
        ON i.invoice_id = pi.invoice_id
INNER JOIN products p
        ON pi.product_id = p.product_id
     WHERE i.buyer_email = 'ana@example.com'
  GROUP BY i.invoice_number

--6
    SELECT i.invoice_number,
        i.purchase_date,
        SUM(pi.total_amount) total
      FROM invoices i
INNER JOIN product_invoice pi
        ON i.invoice_id = pi.invoice_id
  GROUP BY i.invoice_number
  ORDER BY total DESC

--7
    SELECT i.invoice_number,
        i.purchase_date,
        SUM(pi.total_amount) total
      FROM invoices i
INNER JOIN product_invoice pi
        ON i.invoice_id = pi.invoice_id
INNER JOIN products p
        ON pi.product_id = p.product_id
     WHERE i.invoice_number = '1004'
  GROUP BY i.invoice_number