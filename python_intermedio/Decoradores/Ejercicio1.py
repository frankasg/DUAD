
def parameter_printer(func):
    def wrapper(product_name, product_value):
        print(f"El nombre del producto es {product_name}")
        print(f"El valor del producto es {product_value}")
        
        result = func(product_name, product_value)
        print(f"El total del producto con impuesto es {result}")
        return result
    return wrapper

@parameter_printer
def get_product_value_with_taxes(product_name:str, product_value:float):
    taxes = product_value * 0.13
    return product_value + taxes


value = get_product_value_with_taxes("nutella", 25.5)