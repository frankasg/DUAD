from gestor_finanzas_personales.domain.transaction_category import TransactionCategory
from gestor_finanzas_personales.domain.transaction_type import TransactionType
from datetime import date

class Transaction:
	title:str
	created_date:date
	category:TransactionCategory
	amount:float
	type:str

	def __init__(self, title:str, created_date:date, category:TransactionCategory, amount:float, type:str):
		self.title = title
		self.created_date = created_date
		self.category = category
		self.amount = amount
		self.type = type