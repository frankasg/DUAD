import FreeSimpleGUI as sg
from gestor_finanzas_personales.presentation.styles.theme import Theme
from gestor_finanzas_personales.application.finance_manager import FinanceManager
from gestor_finanzas_personales.presentation.views.category_view import show_add_category_window
from gestor_finanzas_personales.presentation.views.transaction_view import show_add_transaction_window
from gestor_finanzas_personales.domain.transaction import Transaction
from gestor_finanzas_personales.infrastructure.storage import save_finance_manager_data, load_finance_manager_data
from gestor_finanzas_personales.infrastructure.csv_manager import export_csv
from datetime import datetime

def total_block(title:str, amount:str, block_bg:str, block_key:str):
	return sg.Column(
		[
			[sg.Text(title, background_color=block_bg, text_color=Theme.MUTED, font=("Arial", 10))],
			[sg.Text(amount,
						background_color=block_bg,
						text_color=Theme.TEXT,
						font=("Arial", 14, "bold"),
						justification="center",
						size=(10, 1),
						pad=(0, 8),
						key=block_key)]
		],
		background_color=block_bg,
		element_justification="center",
		pad=(12, 8)		
	)

def filter_section():
	content = [
		[
			sg.Text(
				"Fecha inicio",
				background_color=Theme.CARD,
				text_color=Theme.MUTED,
				font=("Arial", 10)
			),

			sg.Text(
				datetime.today().strftime("%d/%m/%Y"),
				key="-START_DATE-",
				size=(12, 1),
				background_color=Theme.INPUT_BG,
				text_color=Theme.TEXT,
				border_width=0,
				font=("Arial", 10),
				justification="center"
			),

			sg.CalendarButton(
				"📅",
				target="-START_DATE-",
				format="%d/%m/%Y",
				button_color=(Theme.TEXT, Theme.CARD),
				border_width=0
			),

			sg.Text(
				"Fecha fin",
				background_color=Theme.CARD,
				text_color=Theme.MUTED,
				font=("Arial", 10),
				pad=((15, 5), (0, 0))
			),

			sg.Text(
				datetime.today().strftime("%d/%m/%Y"),
				key="-END_DATE-",
				size=(12, 1),
				background_color=Theme.INPUT_BG,
				text_color=Theme.TEXT,
				border_width=0,
				font=("Arial", 10),
				justification="center"
			),

			sg.CalendarButton(
				"📅",
				target="-END_DATE-",
				format="%d/%m/%Y",
				button_color=(Theme.TEXT, Theme.CARD),
				border_width=0
			),

			sg.Button(
				"Filtrar",
				key="-FILTER-",
				button_color=(Theme.TEXT, Theme.BUTTON_BG),
				border_width=0,
				font=("Arial", 10, "bold"),
				pad=((10, 0), (0, 0)),
				size=(10, 1)
			),

			sg.Button(
				"Limpiar filtro",
				key="-CLEAR_FILTER-",
				button_color=(Theme.TEXT, Theme.BUTTON_BG),
				border_width=0,
				font=("Arial", 10),
				pad=((5, 10), (0, 0)),
				size=(14, 1)
			)
		]
	]

	return sg.Column(
		content,
		background_color=Theme.CARD,
		pad=(0, 10)
	)

def resumen_card(total_expense="$0", total_income="$0", total_balance="$0"):
	left = total_block("Total de Gastos", total_expense, Theme.EXP_BG, "-TOTAL_EXPENSE-")
	center = total_block("Total de Ingresos", total_income, Theme.INC_BG, "-TOTAL_INCOME-")
	right = total_block("Balance", total_balance, Theme.BAL_BG, "-TOTAL_BALANCE-")

	content = sg.Column(
		[
			[
				left,
				sg.VSeparator(pad=(0, 0)),
				center,
				sg.VSeparator(pad=(0, 0)),
				right
			]
		],
		background_color=Theme.CARD,
		element_justification="center",
		pad=(20, 15),
		expand_x=True
	)

	frame = sg.Frame(
		"Resumen de Gastos e Ingresos",
		[[content]],
		background_color=Theme.CARD,
		title_color=Theme.TEXT,
		font=("Arial", 11, "bold"),
		relief=sg.RELIEF_FLAT,
		expand_x=True
	)

	return frame

def table_header_section():
	return sg.Column(
		[
			[
				sg.Text(
					"Tabla de Movimientos",
					background_color=Theme.CARD,
					text_color=Theme.TEXT,
					font=("Arial", 11, "bold"),
					pad=((0, 20), (0, 0))
				),

				sg.Push(background_color=Theme.CARD),

				sg.Button(
					"＋ Agregar Categoría",
					key="-CATEGORY_ADD-",
					button_color=(Theme.TEXT, Theme.BUTTON_BG),
					border_width=0,
					font=("Arial", 10, "bold"),
					size=(18, 1),
					pad=((0, 8), (0, 0))
				),
					
				sg.Button(
					"＋ Agregar Transacción",
					key="-TRANSACTION_ADD-",
					button_color=(Theme.TEXT, Theme.BUTTON_BG),
					border_width=0,
					font=("Arial", 10, "bold"),
					size=(18, 1),
					pad=((0, 8), (0, 0))
				),

				sg.Button(
					"⤓ Exportar CSV",
					key="-CSV_EXPORT-",
					button_color=(Theme.TEXT, Theme.BUTTON_BG),
					border_width=0,
					font=("Arial", 10),
					size=(14, 1)
				)
			]
		],
		background_color=Theme.CARD,
		pad=(12, 10),
		expand_x=True
	)
 
def movements_table():
	headings = ["Fecha", "Categoría", "Título", "Monto", "Tipo"]

	data = []

	return sg.Table(
		values=data,
		headings=headings,
		key="-MOVEMENTS_TABLE-",
		auto_size_columns=False,
		col_widths=[12, 16, 22, 10, 12],
		justification="center",
		num_rows=8,
		background_color=Theme.CARD,
		text_color=Theme.TEXT,
		header_background_color=Theme.BUTTON_BG,
		header_text_color=Theme.TEXT,
		alternating_row_color=Theme.INPUT_BG,
		border_width=0,
		pad=(12, 0),
		expand_x=True  
	)


def table_card():
	content = sg.Column(
		[
			[table_header_section()],
			[movements_table()]
		],
		background_color=Theme.CARD,
		pad=(0, 0),
		expand_x=True
	)

	return sg.Frame(
		"",
		[[content]],
		background_color=Theme.CARD,
		relief=sg.RELIEF_FLAT,
		border_width=0,
		expand_x=True,
		pad=(0, 10)
	)

def build_table_rows(transactions:list[Transaction]):
	result = []
	for r in transactions:		
		new_row = [r.created_date.strftime("%d/%m/%Y"), r.category.name, r.title, str(r.amount), r.type]
		result.append(new_row)
	
	return result

def build_background_color_table_rows(transactions:list[Transaction]):
	result = []
	for i in range(len(transactions)):		
		new_background_color_row = (i, "white",  transactions[i].category.color)
		result.append(new_background_color_row)
	
	return result


def main_window_refresh(window, finance_manager:FinanceManager):
	window["-TOTAL_EXPENSE-"].update(finance_manager.total_expense)
	window["-TOTAL_INCOME-"].update(finance_manager.total_income)
	window["-TOTAL_BALANCE-"].update(finance_manager.total_balance)
	window["-MOVEMENTS_TABLE-"].update(
	values=build_table_rows(finance_manager.transactions),
	row_colors=build_background_color_table_rows(finance_manager.transactions)
)



def main_window():
	try:
		finance_manager = load_finance_manager_data()		
		total_expense = str(finance_manager.total_expense)
		total_income = str(finance_manager.total_income)
		total_balance = str(finance_manager.total_balance)
		bk_original_transactions = finance_manager.transactions		

		layout = [
			[
				sg.Column(
					[
						[filter_section()],
						[resumen_card(f"${total_expense}", f"${total_income}", f"${total_balance}")],
						[table_card()]
					],	
					background_color=Theme.BG,
					pad=(10, 10),
					element_justification="center"
				)
			]
		]

		
		window = sg.Window("Primer programa", layout, background_color=Theme.BG, margins=(20,20), finalize=True)
		main_window_refresh(window, finance_manager)
		
		while True:
			event, values = window.read()
			
			if event == "-CATEGORY_ADD-":
				show_add_category_window(finance_manager)

			if event == "-TRANSACTION_ADD-":
				show_add_transaction_window(finance_manager)
				bk_original_transactions = finance_manager.transactions

			if event == "-FILTER-":
				finance_manager.transactions = FinanceManager.filter_date_range(finance_manager, datetime.strptime(window["-START_DATE-"].get(), "%d/%m/%Y"), datetime.strptime(window["-END_DATE-"].get(), "%d/%m/%Y"))

			if event == "-CLEAR_FILTER-":
				finance_manager.transactions = bk_original_transactions

			if event == "-CSV_EXPORT-":
				export_result = export_csv(finance_manager)

				if export_result:
					sg.popup_quick_message(
						"La información ha sido exitosamente exportada",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)

			if event == sg.WIN_CLOSED:
				finance_manager.transactions = bk_original_transactions
				save_finance_manager_data(finance_manager)
				break
			
			
			main_window_refresh(window, finance_manager)

		window.close()
	
	except Exception as ex:
		print(f"Ha ocurrido un error inesperado. Detalle: {ex}")
		sg.popup_error(
						"Error inesperado",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)

if __name__ == "__main__":
	main_window()