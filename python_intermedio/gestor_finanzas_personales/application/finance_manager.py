from gestor_finanzas_personales.domain.transaction import Transaction
from gestor_finanzas_personales.domain.transaction_type import TransactionType
from gestor_finanzas_personales.domain.transaction_category import TransactionCategory
from datetime import date

class FinanceManager:
	transactions:list[Transaction]
	categories:list[TransactionCategory]
	category_names:list[str]

	def __init__(self):
		self.transactions = []
		self.categories = []
		self.category_names = []

	@property
	def total_expense(self):
		result = 0
		
		for transaction in self.transactions:
				if transaction.type == TransactionType.expense:
						result += transaction.amount
		return result
	
	@property
	def total_income(self):
		result = 0
		
		for transaction in self.transactions:
				if transaction.type == TransactionType.income:
						result += transaction.amount
		return result

	@property
	def total_balance(self):
		return self.total_income - self.total_expense


	def add_transaction(self, title:str, created_date:date, category_name:str, amount:float, type:str):
		transaction_category = self.get_category(category_name)
		transaction_type = TransactionType.expense if TransactionType.expense == type else TransactionType.income
		transaction = Transaction(title, created_date, transaction_category, amount, transaction_type)  
		self.transactions.append(transaction)
	
	def try_to_add_category(self, name:str, color:str):		
		for	c in self.categories:
			if	c.name == name:
				return False
		
		category = TransactionCategory(name, color)		
		self.categories.append(category)
		self.category_names.append(name)
		return True

	def get_category(self, category_name:str):
		for	c in self.categories:
			if	c.name == category_name:
				return c
		return TransactionCategory("","")

	def filter_date_range(self, from_date: date, to_date:date):
		result = []

		for t in self.transactions:
			if t.created_date >= from_date and t.created_date <= to_date:
				result.append(t)

		return result
		