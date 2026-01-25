from datetime import date

class User:
    date_of_birth: date
    age: int
    
    def __init__(self, date_of_birth: date, age: int):
        self.date_of_birth = date_of_birth
        self.age = age

def age_checker(func):
    def wrapper(user: User,):
        if(user.age < 18):
            raise ValueError("Error: La persona debe ser mayor de 18 años.")
        
        func(user)       
    return wrapper

@age_checker
def view_program(user: User):
    print("Estas viendo una programación para mayores de edad")

user = User(date(1987, 11, 28), 38)
view_program(user)


user2 = User(date(2020, 7, 25), 5)
view_program(user2)
