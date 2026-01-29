class BankAccount:    

    def __init__(self, balance: float = 0):
        self.balance = 0

    def deposit(self, value):
        self.balance += value
        

    def withdraw(self, value):
        self.balance -= value

class SavingAccount(BankAccount):
    min_balance : float
    
    def __init__(self, min_balance: float, balance: float = 0):
        super().__init__(balance)
        self.min_balance = min_balance
        

    def withdraw(self, value):
        result = self.balance - value

        if result < self.min_balance:
            raise ValueError("Error si retira esta cantidad su balance va quedar por debajo del balance mínimo")            
        
        return super().withdraw(value)
    

    
saving_account = SavingAccount(5)
saving_account.deposit(10)
print(f"El balance es: {saving_account.balance}")
saving_account.withdraw(3)
print(f"El balance es: {saving_account.balance}")
saving_account.withdraw(3)
print(f"El balance es: {saving_account.balance}")

