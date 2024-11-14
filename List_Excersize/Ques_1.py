# Python program to interchange first and last elements in a

lst = [10,20,50,60]
lst [0] , lst [-1] = lst [-1] , lst [0]
print(lst)


# With Function and user input
def swapped_list(my_list):
    if len(my_list) > 1:
        my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list

user_input = input("Enter list elements separated by spaces: ")
my_list = list(map(int, user_input.split()))
res = swapped_list(my_list)
print(res)


# With Function and without user input

def swapped_list(my_list_2):
    if len(my_list_2) > 1:
        my_list_2[0], my_list_2[-1] = my_list_2[-1], my_list_2[0]
    return my_list_2
my_list_2 = [10,50,60,70]
result = swapped_list(my_list_2)
print(result)