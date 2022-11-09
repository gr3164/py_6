# Задача 2. Задан массив из случайных цифр на 15 элементов.  
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, 
# есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

from random import randint
def V2():
    mylist = [randint(0,9) for _ in range(15)]
    mylist2 = [mylist[i:i+3] for i in range(0,len(mylist))]

    N = input("Введите трех значное число: ")
    while len(N) != 3 and N.isdigit():
        print("Ошибка!")
        N = input("Введите трех значное число: ")

    s = 'Да' if mylist2.count([int(i) for i in N]) else 'нет'
    print(f"{mylist} - {N} -> {s}")

V2()

#===========================================================
def V1():
    mylist = [randint(0,9) for _ in range(15)]
    s = 'Нет'

    def Compare(mylist):
        mylist2 = []
        n = 3
        for i in range(0,len(mylist)):
            mylist2.append(mylist[i:i+3])
            n +=1
        return mylist2

    N = int(input("Введите трех значное число: "))
    while len(str(N)) != 3:
        print("Ошибка!")
        N = int(input("Введите трех значное число: "))
    numbers = [int(i) for i in str(N)]

    if Compare(mylist).count(numbers):
        s = 'Да'

    print(f"{mylist} - {N} -> {s}")

# V1()