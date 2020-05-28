'''Task 1'''

n = int(input("Введите число для анализа: "))

def prime_num_check(n):
    i = 2
    j = 0
    while i**2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if j == 1:
        print ("Это составное число")
    else:
        print ("Это простое число")
prime_num_check(n)

'''Task 2'''

def deviders (n):
    print("Все делители целого числа:", end=" ")
    for i in range(n, 0, -1):
        if (n % i == 0):
            print(i, end=" ")
deviders(n)

'''Task 3'''

def min_max_divider (n):
    min_divider = n
    max_divider = 1
    for i in range(n - 1, 1, -1):
        if (n % i == 0):
            if (min_divider > i):
                min_divider = i
            if (max_divider < i):
                max_divider = i
    print("Минимальный делитель, кроме ""1"" равен:", min_divider)
    print("Максимальный делитель, кроме", n, "равен:", max_divider)
min_max_divider(n)

'''Task 4 (Pro, Light+)'''

def only_prime_dividers (n):
    print("Только простые делители:", end=" ")
    for i in range(n - 1, 1, -1):
        is_simple = 0
        if (n % i == 0):
            for j in range(i - 1, 1, -1):
                if (i % j == 0):
                    is_simple = is_simple + 1
            if (is_simple == 0):
                print(i, end=" ")

only_prime_dividers(n)

print('Задание Light+ 5 реализовн в Light 3')
