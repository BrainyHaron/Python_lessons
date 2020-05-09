# print('Task 1')
#
# x = int(input('Add_First_Num '))
# y = int(input('Add_Second_Num '))
# print('Sum_Num:', x + y, '\n''Diff_Num:', x - y, '\n''Mult_Num:', x * y)
#
#
# print('\n''Task 2')
#
# for x in range (10, 26):
#     print(x+(x+1))
#
#
# print('\n''Task 3')
#
# for x in range(100, 151):
#     if x % 5 == 0:
#         print (x)
#
#
# print('\n''Task 4')
#
# n = int(input("Введите число: "))
#
#
# if n % 2 == 0:
#     print('Введенно четное число')
# if 10 << n << 5:
#     print(n, 'не принадлежит интервалу [5, 10]')
#     if 5 <= n <=10:
#         print(n, 'принадлежит интервалу [5, 10]')
#     elif n > 10:
#         print(n, 'четное и', n, '> 10')
# elif n % 2 != 0:
#     print('Введено не четное число')
#
#
# print('\n''Task 5')
#
# x = 15
# n = 0
# while x <= 22:
#   n += x
#   x += 1
# print(n)
#
#
# print('\n''Task 6')
#
# sum_list = 0
# my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]
# for x in my_list:
#     if type(x) == int:
#         sum_list += x
# print(sum_list)
#
#
# print('\n''Task 7')
#
# my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]
# x = my_list[0]
# for i in range(1, len(my_list)):
#     if my_list[i] > x:
#         x = my_list[i]
# print(x)
#
#
# print('\n''Task 8')
#
# name_dict = {'Наташа': 2, "Алина": 3, "Марат": 15, "Лев": 1, "Валера": 0}
# print(name_dict)
#
# print('\n''Task 9')
#
# name_dict.update({"Рома": 4})
# print(name_dict)
#
#
# print('\n''Pro: Task 1')
#
# for i in range(6):
#     if i != 4:
#         print(i * '@ ')
#
#
# print('\n''Pro: Task 2')
#
# for i in range(10):
#     if i <= 5:
#         print(i * (str(i) + ' '))
#     else:
#         print((10 - i) * (str(i) + ' '))
#
#
# print('\n''Pro: Task 3')
#
# for i in range (11):
#     print('7 * ' + (str(i)), '=', (i*7))
#
#
#
# print('\n''Pro: Task 4')
#
# import random
# cube = list(range(-1, 8))
# random.shuffle(cube)
# d1 = cube.pop()
# d2 = cube.pop()
# print('Значение кубика 1: %d' %d1, '\n' 'Значение кубика 2: %d' %d2)
# count = d1 + d2
# if (1 <= d1 <= 6) and (1 <= d2 <= 6):
#     print('Сумма выпавших значений: %d' % count)
#     if count == 7 or count == 11:
#         print('Я победил!')
#     if count == 2 or count == 3 or count == 12:
#         print('Я проиграл!')
# else:
#     print("Ошибка! Значение на кубике 1 или 2 не входит в интервал [1, 6]")
#
#
#
print('\n''Pro: Task 5')

new_list = []
for i in range(3000, 4301):
    if i % 11 == 0 and i % 5 != 0:
        print(i, end=', ')

#
# print('\n''Pro: Task 6')
#
# sample_list = ["мандаринки", "киви", "лимон"]
# n = int(input('Введите число: '))
# new_list = []
# for n in range(1, n+1):
#     for i in range(len(sample_list)):
#         new_list.append(sample_list[i]+'_'+str(n))
# print(new_list)
#
#
# print('\n''Pro: Task 7')
#
# list_for_pro_task_2 = [35, 0.24, 3 + 4j, "котики", 0.45, (8, 9), "слоники", {"Мадрид": 3, 'Лондон':5}, 23498]
# new_list = []
# for i in range(len(list_for_pro_task_2)):
#     if type(list_for_pro_task_2[i]) == dict:
#         break
# print(i)
#
#
# print('\n''Pro: Task 8')
#
# new_dict = {}
# for i in range(1, 21):
#     new_dict[i] = i ** 2
# print(new_dict)
