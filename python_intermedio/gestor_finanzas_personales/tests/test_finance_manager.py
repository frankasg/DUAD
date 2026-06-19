import pytest
from datetime import date
from gestor_finanzas_personales.domain.transaction_type import TransactionType
from gestor_finanzas_personales.application.finance_manager import FinanceManager

def get_finance_manager_test_data() -> FinanceManager:
	finance_manager = FinanceManager()

	# Categories
	finance_manager.try_to_add_category("Salario", "#2f5f56")
	finance_manager.try_to_add_category("Comida", "#7a3b3b")
	finance_manager.try_to_add_category("Transporte", "#306faa")
	finance_manager.try_to_add_category("Entretenimiento", "#8e44ad")
	finance_manager.try_to_add_category("Freelance", "#16a085")

	# Income
	finance_manager.add_transaction(
		"Pago mensual",
		date(2026, 4, 1),
		"Salario",
		2500,
		TransactionType.income
	)

	finance_manager.add_transaction(
		"Proyecto freelance",
		date(2026, 4, 5),
		"Freelance",
		450,
		TransactionType.income
	)

	# Expenses
	finance_manager.add_transaction(
		"Supermercado",
		date(2026, 4, 3),
		"Comida",
		30,
		TransactionType.expense
	)

	finance_manager.add_transaction(
		"Gasolina",
		date(2026, 4, 7),
		"Transporte",
		40,
		TransactionType.expense
	)

	finance_manager.add_transaction(
		"Cine",
		date(2026, 4, 10),
		"Entretenimiento",
		25,
		TransactionType.expense
	)

	finance_manager.add_transaction(
		"Almuerzo",
		date(2026, 4, 12),
		"Comida",
		25,
		TransactionType.expense
	)

	return finance_manager

def test_total_income_return_sum_of_incomes():
	#Arrange
	finance_manager = get_finance_manager_test_data()
		
	#Acct    
	result = finance_manager.total_income
	#Assert
	assert result == 2950
	
def test_total_expense_return_sum_of_expenses():
	#Arrange
	finance_manager = get_finance_manager_test_data()
		
	#Acct    
	result = finance_manager.total_expense
	#Assert
	assert result == 120

def test_total_balance_return_the_actual_transaction_balance():
	#Arrange
	finance_manager = get_finance_manager_test_data()
		
	#Acct    
	result = finance_manager.total_balance
	#Assert
	assert result == 2830

def test_add_transaction_append_new_transaction_to_transaction_list():
	#Arrange
	finance_manager = FinanceManager()
	finance_manager.try_to_add_category("Comida", "#7a3b3b")
		
	#Acct    
	finance_manager.add_transaction(
		"Almuerzo",
		date(2026, 4, 12),
		"Comida",
		25,
		TransactionType.expense
	)
	#Assert
	assert len(finance_manager.transactions) == 1
	assert finance_manager.transactions[0].title == "Almuerzo"
	assert finance_manager.transactions[0].created_date == date(2026, 4, 12)
	assert finance_manager.transactions[0].category.name == "Comida"
	assert finance_manager.transactions[0].amount == 25
	assert finance_manager.transactions[0].type == TransactionType.expense

def test_try_to_add_category_append_new_category_and_return_true():
	#Arrange
	finance_manager = FinanceManager()
	
	#Acct
	result = finance_manager.try_to_add_category("Comida", "#7a3b3b")

	#Assert
	assert len(finance_manager.categories) == 1
	assert finance_manager.categories[0].name == "Comida"
	assert finance_manager.categories[0].color == "#7a3b3b"
	assert result == True

def test_try_to_add_category_that_already_exists_return_false():
	#Arrange
	finance_manager = FinanceManager()
	
	#Acct
	result = finance_manager.try_to_add_category("Comida", "#7a3b3b")
	result = finance_manager.try_to_add_category("Comida", "#7a3b3b")

	#Assert	
	assert result == False

def test_get_category_if_exist_return_the_category():
	#Arrange
	finance_manager = FinanceManager()
	finance_manager.try_to_add_category("Comida", "#7a3b3b")

	#Acct
	result = finance_manager.get_category("Comida")

	#Act
	assert result.name == "Comida"
	assert result.color == "#7a3b3b"

def test_get_category_if_not_exist_return_empty_category():
	#Arrange
	finance_manager = FinanceManager()
	finance_manager.try_to_add_category("Comida", "#7a3b3b")

	#Acct
	result = finance_manager.get_category("Deporte")

	#Act
	assert result.name == ""
	assert result.color == ""

def test_filter_date_range_return_filtered_transaction_list():
	#Arrange
	finance_manager = get_finance_manager_test_data()	

	#Acct
	result = finance_manager.filter_date_range(date(2026, 3, 5), date(2026, 4, 5))

	#Act
	assert len(result) == 3
 
def test_filter_date_range_between_out_of_range_dates_return_empty_transaction_list():
	#Arrange
	finance_manager = get_finance_manager_test_data()	

	#Acct
	result = finance_manager.filter_date_range(date(2026, 3, 5), date(2026, 3, 6))

	#Act
	assert len(result) == 0