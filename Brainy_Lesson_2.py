#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# for i in range(1, 6):
#     print (str(i) + ') ' + '0' * 100)


'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# a=int(10)
# b=int(5)
# count = 0
# for x in range (1,a+1):
#     y = int(input ("Число " + str(x) + ": " ))
#     while y>0:
#         if y % 10 == b:
#             count += 1
#         y = y // 10
# print("Было введено %d цифр %d" % (count, b))

'''

Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum +=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# multiplication = 1
#
# for i in range(1,11):
#     multiplication *=i
# print(multiplication)



'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 6758437645
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
 '''
# n = int(6758437645)
# sum = 0
# while n > 0:
#     if n % 10 != 0:
#         sum += n % 10
#     n = n // 10
# print ('Сумма цифр', sum)

'''

Задача 7

Найти произведение цифр числа.
'''
# n = int(6758437645)
# mult = 1
# while n > 0:
#     if n % 10 != 0:
#         mult *= (n % 10)
#     n = n // 10
# print('Произведение цифр', mult)

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

# integer_number = int(input())
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9

Найти максимальную цифру в числе
'''



'''
Задача 10

Найти количество цифр 5 в числе
'''
# count = 0
# integer_number = int(input())
# while integer_number>0:
#     if integer_number%10 == 5:
#         count += 1
#     integer_number = integer_number // 10
# print("В введенном числе '%d' цифр 5" % (count))




