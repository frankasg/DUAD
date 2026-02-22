from datetime import datetime

class LoggableMixin:
    def log(self, message: str) -> None:
        print(f"[{datetime.now().isoformat(timespec='seconds')}] {message}")

class SerializableMixin:
    def to_dict(self) -> dict:
        return self.__dict__.copy()

class BankAccount(LoggableMixin, SerializableMixin):
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("El monto del depósito tiene que ser positivo")
        self.balance += amount
        self.log(f"Deposito: +{amount:.2f} -> Balance: {self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("El monto del retiro debe ser mayor a 0")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.log(f"Retiro: -{amount:.2f} -> Balance: {self.balance:.2f}")


acc = BankAccount("Frank", 100)
acc.deposit(50)
acc.withdraw(30)

print(acc.to_dict())
