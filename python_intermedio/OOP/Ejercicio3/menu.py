from common.data_validations_util import is_valid_name, is_valid_section, student_exists, is_valid_grade, is_valid_confirmation_answer
from common.operations_util import student_info_to_dictionary, average
from models.student import Student

def print_main_menu():
    print("""
          -------------------------------------------
          Menú de Opciones
          1. Ingresar estudiante
          2. Información de estudiantes  
          3. Top 3 de estudiantes
          4. Promedio general entre todos los estudiantes
          5. Exportar CSV
          6. Importar CSV
          7. Eliminar estudiante
          8. Lista de estudiantes reprobados          
          9. Salir
          -------------------------------------------
          """)
    
def get_menu_option():
    try:
        menu_option = int(input("Selecciona una las opciones anteriores: "))        

        if menu_option < 1 or menu_option > 9:
            print(f"La opción {menu_option} no corresponde a ninguna de las brindadas anteriormente. Por favor escoja una opción válida.")
        
        return menu_option
    
    except ValueError as value_error:
        print(f"Error [ValueError]: Opción inválida. Detalle: {value_error}")
        return 0
    
def get_name_info():
    display_get_name_info = True 
    name = None

    while display_get_name_info:
        name = input("Ingrese el nombre completo del estudiante: ").strip()
        
        if is_valid_name(name):
            display_get_name_info = False
        
        else:
            print("El nombre completo no puede ser un valor vacío ni contener números o caracteres especiales")
    return name

def get_section_info():
    display_get_section_info = True 
    section = None

    while display_get_section_info:
        section = input("Ingrese la sección a la que pertenece: ").strip()
        
        if is_valid_section(section):
            display_get_section_info = False
        
        else:
            print("Formato de sección invalido. El formato debe tener un número seguido de una letra en mayúscula ejemplo: 10A, 11B, etc")
    return section

def get_grade_info(display_message):
    display_get_grade_info = True 
    grade = None

    while display_get_grade_info:
        try:
            grade = float(input(display_message).strip())
            
            if is_valid_grade(grade):
                display_get_grade_info = False
            
            else:
                print("Valor inválido. Solo son permitidos valores del 0 - 100")
        
        except ValueError as value_error:
            print(f"Error [ValueError]: El valor digitado no corresponde a un número. Detalle: {value_error}")
    
    return grade

def get_user_removal_confirmation():
    display_confirmation_message = True 
    confirmation_answer = None

    while display_confirmation_message:
        try:
            confirmation_answer = int(input("Para confirmar que desea eliminar del sistema al estudiante ingrese 1 para continuar o 2 para cancelar: ").strip())
            
            if is_valid_confirmation_answer(confirmation_answer):
                display_confirmation_message = False
            
            else:
                print("La opción digitada es invalida")
        
        except ValueError as value_error:
            print(f"Error [ValueError]: El valor digitado no corresponde a un número. Detalle: {value_error}")
    
    return confirmation_answer


def get_student_info():
    name = get_name_info()
    section = get_section_info()
    spanish_grade = get_grade_info("Ingrese la nota de español: ")
    english_grade = get_grade_info("Ingrese la nota de inglés: ")
    social_grade = get_grade_info("Ingrese la nota de sociales: ") 
    science_grade = get_grade_info("Ingrese la nota de ciencias: ")
    average_value = average([spanish_grade, english_grade, social_grade, science_grade])

    return Student(name, section, spanish_grade, english_grade, social_grade, science_grade, average_value)    

def get_student_to_remove(students):
    if len(students) == 0:
        print("En estos momentos no existe ningún estudiante registrado")
        return (None,)

    name = get_name_info()
    section = get_section_info()
    user_confirm_action = get_user_removal_confirmation()
    
    if user_confirm_action == 2:
        return (None,)
    
    if not student_exists(students, name, section):
        print(f"No existe un estudiante {name} en la sección {section}")
        return (None,)

    return (name, section)