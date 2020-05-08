# print('Task 1')
#
# x = int(input('Add_First_Num '))
# y = int(input('Add_Second_Num '))
# print('Sum_Num:', x + y, '\n''Diff_Num:', x - y, '\n''Mult_Num:', x * y)

#
# print('\n''Task 2')
# #
# for x in range (10, 26):
#     print(x+(x+1))


# print('\n''Task 3')
#
# for x in range(100, 151):
#     if x % 5 == 0:
#         print (x)


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


# print('\n''Task 5')
#
# x = 15
# n = 0
# while x <= 22:
#   n += x
#   x += 1
# print(n)


print('\n''Task 6')

sum_list = 0
my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]
for x in my_list:
    if type(x) == int:
        sum_list += x
print(sum_list)



