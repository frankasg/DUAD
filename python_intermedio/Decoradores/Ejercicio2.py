from functools import wraps

def is_number(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        for i, arg in enumerate(args):
           if not isinstance(arg, (int, float)):
               raise ValueError(f"El argumento {i} no es un valor numérico")                    
        
        result = func(*args, **kwargs)        
        return result
    return wrapper

@is_number
def get_product_value_with_taxes(numero_producto, product_value):
    print(f"--------- Producto # {numero_producto} ------------------")
    taxes = product_value * 0.13
    return product_value + taxes


value = get_product_value_with_taxes(2, "25.5")
print(f"El total del producto con impuesto es {value}")