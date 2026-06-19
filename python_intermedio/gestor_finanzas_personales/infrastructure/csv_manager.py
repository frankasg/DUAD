import csv
import FreeSimpleGUI as sg
from gestor_finanzas_personales.presentation.styles.theme import Theme
from gestor_finanzas_personales.application.finance_manager import FinanceManager

def export_csv(finance_manager:FinanceManager):
	try:
		if len(finance_manager.transactions) > 0:
			with open('gestor_finanzas.csv', 'w', encoding="utf-8", newline='') as csvfile:
				fieldnames = ["Fecha", "Categoría", "Titulo", "Monto", "Tipo"]
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

				writer.writeheader()
				for transaction in finance_manager.transactions:
					writer.writerow({
						"Fecha": transaction.created_date.strftime("%d/%m/%Y"),
						"Categoría": transaction.category.name,
						"Titulo": transaction.title,
						"Monto": transaction.amount,
						"Tipo": transaction.type
						})
				
				writer.writerow({}) 
				
				writer.writerow({
					"Fecha": "Totales",
					"Categoría": "",
					"Titulo": "",
					"Monto": "",
					"Tipo": ""
					})
				
				writer.writerow({
					"Fecha": "Gastos",
					"Categoría": finance_manager.total_expense,
					"Titulo": "",
					"Monto": "",
					"Tipo": ""
					})

				writer.writerow({
					"Fecha": "Ingresos",
					"Categoría": finance_manager.total_income,
					"Titulo": "",
					"Monto": "",
					"Tipo": ""
					})

				writer.writerow({
					"Fecha": "Balance",
					"Categoría": finance_manager.total_balance,
					"Titulo": "",
					"Monto": "",
					"Tipo": ""
					})
			return True
		
		sg.popup_quick_message(
						"No hay datos para exportar",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)

		return False
	except Exception as ex:
		print(f"Error tratando de exportar CSV. Detalle: {ex}")
		sg.popup_error(
				"Ha ocurrido un error inesperado al tratar de exportar a un formato CSV.",
				background_color=Theme.BG,
				text_color=Theme.TEXT,
				keep_on_top=True
			)
		return False
