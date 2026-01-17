from common.operations_util import order_by_average
from common.data_validations_util import student_exists
from models.student import Student

def add_student_info(students : list, student_info : Student):
    if student_exists(students, student_info.name, student_info.section):
        print(f"El estudiante {student_info.name} ya existe en la sección {student_info.section}")
        return
    
    students.append(student_info)

def print_all_students(students: list):
    table_width = 105
    print("\n" + "=" * table_width)
    print("INFORMACiÓN DE ESTUDIANTES".center(table_width))
    print("=" * table_width)

    header = (
        f"{"Nombre":<30}"
        f"{"Sección":<10}"
        f"{"Nota Español":<15}"
        f"{"Nota Inglés":<15}"
        f"{"Nota Sociales":<15}"
        f"{"Nota Ciencias":<15}"
    )
    print(header)
    print("-" * table_width)

    for student in students:
        print(
            f"{student.name:<30}"
            f"{student.section:<10}"
            f"{student.spanish:<15}"
            f"{student.english:<15}"
            f"{student.social:<15}"
            f"{student.science:<15}"
        )

    print("=" * table_width)

def print_top3_students(students : list):
    students_len = len(students) 
    if students_len == 0:
        print("Actualmente no hay registro de estudiantes")
        return
    top = min(3, students_len)
    ordered_students = order_by_average(students)

    table_width = 105
    print("\n" + "=" * table_width)
    print("TOP 3 DE ESTUDIANTES".center(table_width))
    print("=" * table_width)

    header = (
        f"{"Nombre":<30}"
        f"{"Sección":<10}"
        f"{"Promedio":<15}"
    )
    print(header)
    print("-" * table_width)

    for i in range(top):
        print(
            f"{ordered_students[i].name:<30}"
            f"{ordered_students[i].section:<10}"
            f"{ordered_students[i].average:<15}"            
        )

    print("=" * table_width)

def print_general_average(students : list):
    students_len = len(students)
    if(students_len == 0):
        print("Debe existir al menos 1 estudiante para poder mostrar el promedio general")
        return
    
    general_average = 0
    all_grades_total = 0

    for student in students:
        all_grades_total += student.average 
    
    general_average = all_grades_total / students_len

    table_width = 105
    print("\n" + "=" * table_width)
    print(f"El promedio general entre todos los estudiantes es: {general_average:.2f}".center(table_width))
    print("=" * table_width)

def remove_student(students:list, name, section):    
    student = None

    for s in students:
        if s.name == name and s.section == section:
            student = s    
    
    if student is None:
        print(f"El estudiante {name} en la sección {section} no existe")
        return
    
    students.remove(student)
    print(f"El estudiante {name} en la sección {section} ha sido eliminado del sistema")

def print_failed_students(students: list):
    if not any(s.spanish < 60 or s.english < 60 or s.social < 60 or s.science < 60 for s in students):
        print("No hay estudiantes reprobados para mostrar en estos momentos")
        return

    table_width = 105
    print("\n" + "=" * table_width)
    print("ESTUDIANTES REPROBADOS".center(table_width))
    print("=" * table_width)

    header = (
        f"{"Nombre":<30}"
        f"{"Sección":<10}"
        f"{"Nota Español":<15}"
        f"{"Nota Inglés":<15}"
        f"{"Nota Sociales":<15}"
        f"{"Nota Ciencias":<15}"
    )
    print(header)
    print("-" * table_width)

    for student in students:
        if student.spanish < 60 or student.english < 60 or student.social < 60 or student.science < 60 : 
            spanish = student.spanish if student.spanish < 60 else "-"
            english = student.english if student.english < 60 else "-"
            social  = student.social  if student.social  < 60 else "-"
            science = student.science if student.science < 60 else "-"

            print(
                f"{student.name:<30}"
                f"{student.section:<10}"
                f"{str(spanish):<15}"
                f"{str(english):<15}"
                f"{str(social):<15}"
                f"{str(science):<15}"
            )
    print("=" * table_width)

