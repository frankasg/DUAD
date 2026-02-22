import math

#Ejercicio 1
print("Ejercicio  1: ---------------------------------------------")

def my_first_function():
    print("First function")
    my_second_function()
        

def my_second_function():        
    print("Second function")


my_first_function()

#Ejercicio 2
print("Ejercicio 2: ---------------------------------------------")

def local_scope_function():
    name = "Frank"

# print(name) aca vemos como se refleja que name no es valido en el scope
        

my_global_def = 1987
print(my_global_def)

def update_global_var(value):
    global my_global_def
    my_global_def = value
        
update_global_var(2025)
print(my_global_def)

#Ejercicio 3
print("Ejercicio 3: ---------------------------------------------")

def sum_numbers(numbers):
    result = 0
    for number in numbers:
        result = result + number
    return result

print(sum_numbers([4, 6, 2, 29] )) 

#Ejercicio 4
print("Ejercicio 4: ---------------------------------------------")

def reverse_string(value):
    result = ""

    for index in range(len(value)-1, -1, -1):
        result = result + value[index]
    
    return result

print(reverse_string("Hola mundo"))

#Ejercicio 5
print("Ejercicio 5: ---------------------------------------------")

def count_upper_and_lower_letters(value):
    upper_cases = 0
    lower_cases = 0
    
    for index in range(len(value)):
        if not value[index].isalpha():
            continue

        if value[index].isupper():
            upper_cases += 1
            continue
        
        lower_cases += 1

    return f"There's {upper_cases} upper cases and {lower_cases} lower cases"

print(count_upper_and_lower_letters("Hola Mundo"))

#Ejercicio 6
print("Ejercicio 6: ---------------------------------------------")

def order_words(value):
    words = value.split("-")    
    words.sort()
    result = ""
    
    for item in words:
        result = result + item + "-"
    
    return result[0:len(result)-1]

print(order_words("python-variable-funcion-computadora-monitor"))


#Ejercicio 7
print("Ejercicio 7: ---------------------------------------------")



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    result = []

    for number in numbers:
        if is_prime(number):
            result.append(number)
    
    return result

print(get_prime_numbers([1, 4, 6, 7, 13, 9, 67]))

