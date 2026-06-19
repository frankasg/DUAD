import pickle
import FreeSimpleGUI as sg
from gestor_finanzas_personales.presentation.styles.theme import Theme
from gestor_finanzas_personales.application.finance_manager import FinanceManager

def save_finance_manager_data(finance_manager: FinanceManager):     
	try:
		with open("data.pkl", "wb") as f:
			pickle.dump(finance_manager, f)
	except Exception as ex:
		print(f"Error tratando de guardar archivo. Detalle: {ex}")
		sg.popup_error(
			"Ha ocurrido un error inesperado al trata de guardar la información.",
			background_color=Theme.BG,
			text_color=Theme.TEXT,
			keep_on_top=True
			)


def load_finance_manager_data():
	try:
		with open("data.pkl", "rb") as f:
			loaded_data = pickle.load(f)	
		return loaded_data
	except FileNotFoundError:
		finance_manager = FinanceManager()
		return finance_manager
	except Exception as ex:
		print(f"Error tratando de cargar archivo. Detalle: {ex}")
		sg.popup_error(
			"Ha ocurrido un error inesperado al trata de cargar la información.",
			background_color=Theme.BG,
			text_color=Theme.TEXT,
			keep_on_top=True
			)
	
