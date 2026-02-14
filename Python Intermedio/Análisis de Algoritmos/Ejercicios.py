#Ejercicio1

def bubble_sort(list:list): #O(n^2)
    for outer_index in range(len(list)-1): #O(n)
        list_updated = False #O(1)
                
        for inner_index in range(len(list)-1-outer_index): #O(n^2)
            if list[inner_index] > list[inner_index+1]: #O(1)
                backup_value = list[inner_index] #O(1)
                list[inner_index] = list[inner_index+1] #O(1)
                list[inner_index+1] = backup_value #O(1)

                if not list_updated: #O(1)
                    list_updated = True #O(1)
        
        if list_updated == False: #O(1)
            break #O(1)

    return list #O(1)

#Ejercicio2

def print_numbers_times_2(numbers_list): #O(n)
	for number in numbers_list: #O(n)
		print(number * 2) #O(1)
          
def check_if_lists_have_an_equal(list_a, list_b): #O(n^2)
	for element_a in list_a: #O(n)
		for element_b in list_b: #O(n^2)
			if element_a == element_b: #O(1)
				return True #O(1)
				
	return False #O(1)

def print_10_or_less_elements(list_to_print): #O(1)
	list_len = len(list_to_print) #O(1)
	for index in range(min(list_len, 10)): #O(1) 
		print(list_to_print[index]) #O(1)
		
def generate_list_trios(list_a, list_b, list_c): #O(n^3)
	result_list = [] #O(1)
	for element_a in list_a: #O(n)
		for element_b in list_b: #O(n^2)
			for element_c in list_c: #O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}') #O(1)
				
	return result_list #O(1)