from menu import print_main_menu, get_menu_option, get_student_info, get_student_to_remove
from actions import add_student_info, print_all_students, print_top3_students, print_general_average, remove_student, print_failed_students
from data import export_csv, import_students_from_csv
from models.student import Student

def main():    
    try:
        program_terminated = False
        headers = ["name", "section", "spanish", "english", "social", "science"]
        students = []

        while not program_terminated:     
            print_main_menu()
            menu_option = get_menu_option()                        
            
            match menu_option:
                case 1:
                    student_info = get_student_info()
                    add_student_info(students, student_info)
                case 2:
                    print_all_students(students)
                case 3:
                    print_top3_students(students)
                case 4:
                    print_general_average(students)
                case 5:                    
                    export_csv(students, headers)
                case 6:
                    import_result = import_students_from_csv()

                    if import_result[0] == True:
                        students = import_result[1]
                case 7:
                    student_to_remove = get_student_to_remove(students)

                    if(student_to_remove[0] is not None):
                        remove_student(students, student_to_remove[0], student_to_remove[1])
                case 8:
                    print_failed_students(students)
                case 9:
                    program_terminated = True
                    continue                
    
    except Exception as ex:
        print(f"Ha ocurrido un error inesperado. Detalle: {ex}")

if __name__ == "__main__":
    main()