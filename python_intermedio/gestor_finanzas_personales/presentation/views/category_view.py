import FreeSimpleGUI as sg
from gestor_finanzas_personales.presentation.styles.theme import Theme
from gestor_finanzas_personales.application.finance_manager import FinanceManager


def show_add_category_window(finance_manager:FinanceManager):
	layout = [
		[
			sg.Column(
				[
					[
						sg.Text(
							"Agregar Nueva Categoría",
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
							"Nombre de la categoría",
							font=("Arial", 11),
							text_color=Theme.TEXT,
							background_color=Theme.CARD,
							pad=((0, 0), (0, 5))
						)
					],
					[
						sg.Input(
							key="-CATEGORY_NAME-",
							background_color=Theme.INPUT_BG,
							text_color=Theme.TEXT,
							border_width=0,
							font=("Arial", 11),
							size=(30, 1)
						)
					],

					[
						sg.Text(
							"Color",
							font=("Arial", 11),
							text_color=Theme.TEXT,
							background_color=Theme.CARD,
							pad=((0, 0), (15, 5))
						)
					],
					[
						sg.Text(
							key="-CATEGORY_COLOR-",
							text="#4a90e2",							
							background_color=Theme.INPUT_BG,
							text_color=Theme.TEXT,
							font=("Arial", 11),
							size=(22, 1),
						),

						sg.ColorChooserButton(
							"🎨",
							target="-CATEGORY_COLOR-",
							button_color=(Theme.TEXT, Theme.BUTTON_BG),
							border_width=0,
							size=(4, 1),
							pad=((8, 0), (0, 0))
						)
					],

					[
						sg.Push(background_color=Theme.CARD),
						sg.Button(
							"Guardar",
							key="-SAVE_CATEGORY-",
							button_color=(Theme.TEXT, Theme.INC_BG),
							border_width=0,
							font=("Arial", 11, "bold"),
							size=(10, 1),
							pad=((0, 8), (20, 0))
						),
						sg.Button(
							"Cancelar",
							key="-CANCEL_CATEGORY-",
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
		"Agregar Categoría",
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

			if event in (sg.WIN_CLOSED, "-CANCEL_CATEGORY-"):
				break

			if event == "-SAVE_CATEGORY-":
				category_name = values["-CATEGORY_NAME-"].strip()
				category_color = window["-CATEGORY_COLOR-"].get()

				if not category_name:
					sg.popup_error(
						"Debes ingresar un nombre para la categoría.",
						background_color=Theme.BG,
						text_color=Theme.TEXT,
						keep_on_top=True						
					)
					continue
				
				if not finance_manager.try_to_add_category(category_name, category_color):
					sg.popup_error(
							"Ya existe una categoría con ese nombre",
							background_color=Theme.BG,
							text_color=Theme.TEXT,
							keep_on_top=True							
						)
					continue
				
			break
		except	Exception as ex:
			print(f"Ha ocurrido un error inesperado en el category view. Detalle: {ex}")
			sg.popup_error(
					"Error inesperado",
					background_color=Theme.BG,
					text_color=Theme.TEXT,
					keep_on_top=True
				)

	window.close()
	