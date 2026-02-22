from models.student import Student

def student_info_to_dictionary(student_info, values):    
    headers = ["name", "section", "spanish", "english", "social", "science", "average"]

    for index in range(len(headers)):
        student_info[headers[index]] = values[index]

def average(grades):
    total = 0
    result = 0

    for grade in grades:
        total += grade
    
    if total == 0:
        return result
    
    result = total / len(grades)
    return result

def order_by_average(students):
    return sorted(students, key=lambda item: item.average, reverse=True)

def generate_average(students):
    for i in range(len(students)):
        students[i]["average"] = average([students[i]["spanish"], students[i]["english"], students[i]["social"], students[i]["science"]])

def to_dict_list(students: Student):
    result = []

    for s in students:
        student_dict = vars(s)
        result.append(student_dict)
    return result
