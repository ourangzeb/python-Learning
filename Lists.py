

# Lists in python can hold a lot of information of multiple objects in python>?

# Python array will have only one datatype of elements at consecutive memory location


number = [1,2,34,45,6,7,8]
# print list through for each loop
def print_lists(list):
    for value in list:
        print(value)
    return

# print each element in list through while loop

def list_numbers_while_loop(n):
    i = 0
    while i < len(n):
        print(n[i]*4)
        i += 1
    return

list_numbers_while_loop(number)

print(number)