

# Lists in python can hold a lot of information of multiple objects in python>?

# Python array will have only one datatype of elements at consecutive memory location
# #listssssss

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
# Lets modify the array.........

a = [11,3,45,45655,56766,67676,787]

a.append(23432)



a.append("2lkjsdkfs")

print_lists(a)

a + [2,34,34,4,56,6,78,834]
print(a)

b =  a + [2,34,34,4,56,6,78,834]
print(b)



def square_list(list):
    i = 0 ;

    while i < len(list):
        list[i] = list[i] * list[i]
        i +=1

    return list

# print(square_list([1,2,3,54]))


def sum_list(lists):

     total = 0
     i = 0
     while i <len(lists):
         total +=  lists[i] 
         i +=1
     return total

print(sum_list([21,34,4556]))
