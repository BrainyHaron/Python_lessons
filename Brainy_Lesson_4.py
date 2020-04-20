# Functions

# def add(x, y):
#     return x+y
# help (add)
#
# print (add(100, 101))
# print (add('Alex', 'Kate'))
#
# def f1(n):
#     def f2(m):
#         return n+m
#     return f2
# new_f = f1(100)
# print(new_f(250))
#
# def f ():
#     pass
#
# print (f())

# Arguments

# def add(x, y, z = 10):
#     """
#
#     :param x:
#     :param y:
#     :return:
#     """
#    return x+y+z
#
# print(add(x, y, z = 10))

#
# def ident(x):
#     return x
#
# print(ident(10))
#
# print((lambda x: x)(10))
#
# ident_lamda = lambda x: x
# print (ident_lamda (10))
#
# car = lambda brend, volume_engine, price: f'Car: {brend.title()}, Volume engine: {volume_engine}, Price {price}'
# print (car('volvo', 1.5, 130000))
#
# print(type(ident_lamda), type(ident))
from typing import Any, Iterator, List


# name = ['Маша', 'Петя', 'Саша')]
# name_lengths = map (len, name)
# print(name_lengths)
#
# squares = map(lambda x: x*x, [1, 2, 3, 4])
# print(squares)


# from functools import reduce
# sum_all = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# print(sum_all)
#
#
# # map
# def miles_to_km(miles):
#     return miles*1.6
#
# mile_dist = [1.0, 1.6, 2.3]
#
# km_dist = list(map(miles_to_km, mile_dist))
# print(type(km_dist), km_dist)
#
#
# km_dist = list(map(lambda x:1.6*x, mile_dist))
# print(type(km_dist), km_dist)
#
#
#
#
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_3 = list(map(lambda x, y: x*y, list_1, list_2))
# print(list_3)
#
# from functools import reduce
#
# list_temp =[43, 12, 41, 100, 101, 4]
# max = reduce(lambda a, b: a if a>b else b, list_temp)
# print(max)
#
# list_50 = list(filter(lambda x: x %10 == 1, list_temp))
# print(list_50)
#
# #sorted
#
# list_temp_sort = sorted(list_temp)
# print(list_temp_sort)
#
# list_temp_reverse = sorted(list_temp, reverse = True)
# print(list_temp_reverse)
#
# #key
#
# list_names = ('Kate', 'Dima', 'Ivan', 'Mike')
# list_temp_sort= sorted(list_names)
# print(list_temp_sort)
#
# list_temp_sort_key = sorted(list_names, key = lambda x: x[3])
# print(list_temp_sort_key)
#
#
# global_var = 10
#
# def function_example(local_var_1, local_var_2):
#     print(local_var_1, local_var_2, global_var)
#
# function_example(11, 12)
#
#
#
# def function_example_1(local_var_1, local_var_2):
#     global global_var
#     global_var = 20
#     print(local_var_1, local_var_2, global_var, id(global_var))
#
#
# function_example_1(13, 14)
# print(global_var, id(global_var))
#
# # nonlocal
#
# def counter ():
#     num = 0
#     def plus_one():
#         nonlocal num
#         num += 1
#         return num
#     return plus_one
# count = counter()
#
# print(count)
# print(count())
# print(count())


#factorial

# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num*fact(num-1)
# print(fact(10))
#
# factorial = 1
# for i in range(1, 11):
#     factorial *= i
# print(factorial)


#a^b

# def degree(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a* degree(a, b-1)
# print(degree(2, 10))
#
#
# deg = 1
# for i in range(1, 11):
#     deg *= 2
# print(deg)

#
# name = open('Names.txt', 'r', encoding='UTF-8')
# list_names = name.read().split()
# list_temp_sort = sorted(list_names)



from random import choices
name = open('Names.txt', 'r', encoding='UTF-8')
list_names = name.read().split()
# print(list_names)
def choice_name(names, length_list):
    return choices(names, k=length_list)
task_list = sorted(choice_name(list_names, length_list = 100))

def most_frequently (names):
    word = {}
    for name in names:
        word[name] = word.get(name, 0) + 1
    word = list(word.items())
    word.sort(key=lambda x: x[1], reverse=True)
    return word[0][0]

print('Light_1:')
print(task_list)
print('Light_2:')
print(most_frequently(list_names))
print('Light_3:')



