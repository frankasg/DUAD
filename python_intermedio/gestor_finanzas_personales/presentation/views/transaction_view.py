import FreeSimpleGUI as sg

from gestor_finanzas_personales.presentation.styles.theme import Theme
from gestor_finanzas_personales.application.finance_manager import FinanceManager
from gestor_finanzas_personales.domain.transaction import Transaction
from datetime import datetime


def show_add_transaction_window(finance_manager: FinanceManager):
	category_names = finance_manager.category_names

	if(len(category_names) == 0):
		sg.popup_error(
			"Debes Ingresar al menos una categoría antes de continuar",
			background_color=Theme.BG,
			text_color=Theme.TEXT,
			keep_on_top=True
			)
		return

	layout = [
		[
			sg.Column(
				[
					[
						sg.Text(
							"Agregar Nueva Transacción",
							font=("Arial", 14, "bold"),
							text_color=Theme.TEXT,
							background_color=Theme.CARD,
							justification="center",
							expand_x=True,
							pad=((0, 0), (10, 20))
						)
					],

					[
						sg.Text(
							"Título",
							font=("Arial", 11),
							text_color=Theme.TEXT,
							background_color=Theme.CARD,
							pad=((0, 0), (0, 5))
						)
					],
					[
						sg.Input(
							key="-TRANSACTION_TITLE-",
							background_color=Theme.INPUT_BG,
							text_color=Theme.TEXT,
							border_width=0,
							font=("Arial", 11),
							size=(30, 1)
						)
					],

					[
						sg.Text(
							"Categoría",
							font=("Arial", 11),
							text_color=Theme.TEXT,
							background_color=Theme.CARD,
							pad=((0, 0), (15, 5))
						)
					],
					[
						sg.Combo(
							values=category_names,
							key="-TRANSACTION_CATEGORY-",
							background_color=Theme.INPUT_BG,
							text_color=Theme.TEXT,
							button_background_color=Theme.BUTTON_BG,       							
							font=("Arial", 11),
							readonly=True,
							size=(28, 1)
						)
					],

					[
						sg.Text(
							"Monto",
							font=("Arial", 11),
							text_color=Theme.TEXT,
							background_color=Theme.CARD,
							pad=((0, 0), (15, 5))
						)
					],
					[
						sg.Input(
							key="-TRANSACTION_AMOUNT-",
							background_color=Theme.INPUT_BG,
							text_color=Theme.TEXT,
							border_width=0,
							font=("Arial", 11),
							size=(30, 1)
						)
					],

					[
						sg.Text(
							"Tipo",
							font=("Arial", 11),
							text_color=Theme.TEXT,
							background_color=Theme.CARD,
							pad=((0, 0), (15, 5))
						)
					],
					[
						sg.Combo(
							values=["Gasto", "Ingreso"],
							key="-TRANSACTION_TYPE-",
							background_color=Theme.INPUT_BG,
							text_color=Theme.TEXT,
							button_background_color=Theme.BUTTON_BG,							
							font=("Arial", 11),
							readonly=True,
							size=(28, 1)
						)
					],
					[sg.Text(
						"Fecha", 
						background_color=Theme.CARD, 
						text_color=Theme.MUTED,
						font=("Arial", 10)
						)
					],
					[
						sg.Text(datetime.today().strftime("%d/%m/%Y"), key="-TRANSACTION_DATE-", size=(12, 1), background_color=Theme.INPUT_BG,	text_color=Theme.TEXT, font=("Arial", 10), justification="center"),
						sg.CalendarButton("📅", target="-TRANSACTION_DATE-", format="%d/%m/%Y", button_color=(Theme.TEXT, Theme.CARD), border_width=0)
					],
					[
						sg.Push(background_color=Theme.CARD),
						sg.Button(
							"Guardar",
							key="-SAVE_TRANSACTION-",
							button_color=(Theme.TEXT, Theme.INC_BG),
							border_width=0,
							font=("Arial", 11, "bold"),
							size=(10, 1),
							pad=((0, 8), (20, 0))
						),
						sg.Button(
							"Cancelar",
							key="-CANCEL_TRANSACTION-",
							button_color=(Theme.TEXT, Theme.SECONDARY_BUTTON),
							border_width=0,
							font=("Arial", 11),
							size=(10, 1),
							pad=((0, 0), (20, 0))
						),
						sg.Push(background_color=Theme.CARD)
					]
				],
				background_color=Theme.CARD,
				pad=(20, 20)
			)
		]
	]

	window = sg.Window(
		"Agregar Nueva Transacción",
		layout,
		modal=True,
		keep_on_top=True,
		finalize=True,
		background_color=Theme.BG,
		element_justification="center",
		use_default_focus=False
	)

	result = None

	while True:
		try:
			event, values = window.read()

			if event in (sg.WIN_CLOSED, "-CANCEL_TRANSACTION-"):
				break

			if event == "-SAVE_TRANSACTION-":
				title = values["-TRANSACTION_TITLE-"].strip()
				category_name = values["-TRANSACTION_CATEGORY-"]
				amount_text = values["-TRANSACTION_AMOUNT-"].strip()
				transaction_type = values["-TRANSACTION_TYPE-"]
				transaction_date = datetime.strptime(window["-TRANSACTION_DATE-"].get(), "%d/%m/%Y") 

				if not title:
					sg.popup_error(
						"Debes ingresar un título.",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)
					continue

				if not category_name:
					sg.popup_error(
						"Debes seleccionar una categoría.",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)
					continue

				if not amount_text:
					sg.popup_error(
						"Debes ingresar un monto.",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)
					continue

				try:
					amount = float(amount_text)
				except ValueError:
					sg.popup_error(
						"El monto debe ser numérico.",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)
					continue

				if not transaction_type:
					sg.popup_error(
						"Debes seleccionar un tipo.",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)
					continue
				
				if datetime.today() < transaction_date:
					sg.popup_error(
						"La fecha seleccionada no puede ser en el futuro.",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True
					)
					continue
				
				finance_manager.add_transaction(title, transaction_date, category_name, amount, transaction_type)		
				break
		except	Exception as ex:
			print(f"Ha ocurrido un error inesperado en el transaction view. Detalle: {ex}")
			sg.popup_error(
					"Error inesperado",
					background_color=Theme.BG,
					text_color=Theme.TEXT,
					keep_on_top=True
				)

	window.close()
	