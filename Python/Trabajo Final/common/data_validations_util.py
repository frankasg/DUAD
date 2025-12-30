import re

def is_valid_name(name):
    pattern = r"^[^0-9]+$"

    if not bool(re.match(pattern, name)):
        return False    
    return True

def is_valid_section(section):
    pattern = r"^\d+[A-Z]$"

    if not bool(re.match(pattern, section)):
        return False    
    return True

def student_exists(students:list, name, section):
    for student in students:
        if student["name"].lower() == name.lower() and student["section"] == section:
            return True
    return False

def is_valid_grade(grade):
    if grade < 0 or grade > 100:
        return False
    return True

def is_valid_confirmation_answer(answer):
    try:
        return int(answer) in (1, 2)
    except (ValueError, TypeError):
        return False

def is_valid_student_list_data(students):
    try:
    
        if len(students) == 0:
            print("Archivo csv invalido, no hay datos para importar")
            return False

        for student in students:
            if not is_valid_name(student["name"]):
                print(f"El nombre: {student["name"]} no puede ser valor vacío ni contener números")
                return False
            
            elif not is_valid_section(student["section"]):
                print(f"La sección: {student["section"]} posee un formato incorrecto")
                return False

            elif not is_valid_grade(float(student["spanish"])):
                print(f"La nota: {student["spanish"]} del estudiante {student["name"]} es invalida")
                return False
            
            elif not is_valid_grade(float(student["english"])):
                print(f"La nota: {student["english"]} del estudiante {student["name"]} es invalida")
                return False
            
            elif not is_valid_grade(float(student["social"])):
                print(f"La nota: {student["social"]} del estudiante {student["name"]} es invalida")
                return False
            
            elif not is_valid_grade(float(student["science"])):
                print(f"La nota: {student["science"]} del estudiante {student["name"]} es invalida")
                return False
        return True
        
    except ValueError as value_error:
        print(f"Error [ValueError]: El archivo contiene notas que no corresponden a un valor numérico. Detalle: {value_error}")
        
    
    except Exception as ex:
        print(f"Ha ocurrido un error inesperado. Detalle: {ex}")
        return False
    

def student_exist_more_than_one(students):
    students_to_validate = set()

    for s in students:
        keys = (s["name"], s["section"])

        if keys in students_to_validate:
            print("Error: Uno o mas estudiantes se encuentran duplicados en el archivo que intenta importar")
            return True
        
        students_to_validate.add(keys)
    
    return False




