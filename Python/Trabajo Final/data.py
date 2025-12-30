import csv
from common.data_validations_util import is_valid_student_list_data, student_exist_more_than_one
from common.operations_util import generate_average

def export_csv(students : list, headers: list):
    if len(students) == 0:
        print("No hay datos para exportar")
        return

    with open("Students.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers, extrasaction="ignore") 
        writer.writeheader()
        writer.writerows(students)
    
    print("El archivo CSV ha sido creado con el nombre de Students")

def import_students_from_csv():
    try:
        with open("Students.csv", "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            imported_students = list(reader)        
      
        if student_exist_more_than_one(imported_students) or not is_valid_student_list_data(imported_students):
            return (False, None) 

        for i in range(len(imported_students)):
            imported_students[i]["spanish"] = float(imported_students[i]["spanish"])
            imported_students[i]["english"] = float(imported_students[i]["english"])
            imported_students[i]["social"] = float(imported_students[i]["social"])
            imported_students[i]["science"] = float(imported_students[i]["science"])            

        generate_average(imported_students)
        print("Archivo importado exitosamente")
        return (True, imported_students)

    except FileNotFoundError as file_not_found_error:
        print(f"Error [FileNotFoundError]: Archivo no encontrado, debe primero exportar un csv para poderlo importar: {file_not_found_error}")
        return (False, None)
