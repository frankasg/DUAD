from datetime import date

class User:
    date_of_birth: date    
    
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth
        
    
    @property
    def age(self):
         today = date.today()
         return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))        

def age_checker(func):
    def wrapper(user: User,):
        if(user.age < 18):
            raise ValueError("Error: La persona debe ser mayor de 18 años.")
        
        func(user)       
    return wrapper

@age_checker
def view_program(user: User):
    print("Estas viendo una programación para mayores de edad")

user = User(date(1987, 11, 28))
view_program(user)


user2 = User(date(2020, 7, 25))
view_program(user2)
