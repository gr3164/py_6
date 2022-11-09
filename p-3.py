# Задача 3. Найдите все простые несократимые дроби, 
# лежащие между 0 и 1, знаменатель которых не превышает 11.

from fractions import Fraction

def V2():
    s2 = []
    print('\n'.join(set([str(Fraction(i,j)) for i in range(1,11) for j in range(1,12) if i < j and  not s2.count(Fraction(i,j))])))

V2()

# ==================================================
def V1():
    s = []
    for i in range(1,11):
        for j in range(1,12):
            if i < j and  not s.count(Fraction(i,j)):
                s.append(str(Fraction(i,j)))
    print('\n'.join(set(s)))

# V1()