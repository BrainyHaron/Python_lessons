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

