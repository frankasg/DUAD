def bubble_sort(list:list):
    for outer_index in range(len(list)-1):
        list_updated = False
                
        for inner_index in range(len(list)-1-outer_index):
            if list[inner_index] > list[inner_index+1]:
                backup_value = list[inner_index]
                list[inner_index] = list[inner_index+1]
                list[inner_index+1] = backup_value

                if not list_updated:
                    list_updated = True
        
        if list_updated == False:
            break

    return list

unordered_list = [5, 1, 4, 2, 8, 3]
print(unordered_list)

ordered_list = bubble_sort(unordered_list)
print(ordered_list)
