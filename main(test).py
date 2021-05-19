import unittest
# Begin25
"""
x = int(input("Введите значение x = \n"))

y = 3*(x**6) - 6*(x**2) - 7

assert x > 0

print(y, end='\n')
"""
# Begin20
"""
x1 = int(input("Введите значение x1 = \n"))
x2 = int(input("Введите значение x2 = \n"))
y1 = int(input("Введите значение y1 = \n"))
y2 = int(input("Введите значение y2 = \n"))

z = (((x2-x1)**2) + ((y2-y1)**2))**1/2
assert z>0
print(z, end='\n')
"""
#Integer20
"""
N = int(input("Введите кол-во секунд, прошедших с начала дня = \n"))
day = 86400
z = (86400-N)
x = int(z/3600)
assert x>0
print("Кол-во полных часов: ",x, end='\n')
"""
#Integer25
"""
K = int(input("Введите номер дня = \n"))
z = pow(K+3,1,7)
assert z>0
print("Номер дня недели: ",z, end='\n')
"""
#Boolean10
"""
A = int(input("Введите число A = \n"))
B = int(input("Введите число B = \n"))

C = A+B
assert C>0
print(C)
if C%2 == 1 :
    print("Ровно одно из числе A и B нечетное")
else:
    print("Не подходит")
"""
#Boolean20
"""
N = int(input("Введите трёхзначное число = \n"))
if (N>99 and N<1000):
    A = int(N/100)
    B = int((N/10)%10)
    C = int(N%10)
    assert A > 0
    assert B > 0
    assert C > 0
    if (A != B and A != C and B != C):
        print("Все цифры данного числа разные")
    else:
        print("Неверное число")
"""
#If6
"""
A = int(input("Введите число A = \n"))
B = int(input("Введите число B = \n"))
assert A+B>0
if A>B:
    print("A = ",A, end='\n')
else:
    print("B = ",B, end='\n')
"""
#If15
"""
A = int(input("Введите число A = \n"))
B = int(input("Введите число B = \n"))
C = int(input("Введите число C = \n"))

if A+B>(B+C) and (A+C):
    print("A+B = ", A + B, end='\n')
if A+C>(B+C) and (A+B):
    print("A+C = ", A + C, end='\n')
if B+C>(A+C) and (A+B):
    print("B+C = ", B + C, end='\n')
"""
#Case4
"""
def switch_demo(argument):
    switcher = {
    1: '31 день',
    2: '28 дней',
    3: '31 день',
    4: '30 дней',
    5: '31 день',
    6: '30 дней',
    7: '31 день',
    8: '31 день',
    9: '30 дней',
    10: '31 день',
    11: '30 дней',
    12: '31 день',
    }
    print(switcher.get(argument, "Не существующий месяц"))
switch_demo(int(input("введите от 1 до 12 \n")))
"""
#Case18
"""
def hundred(argument):
    switcher = {
        1: "Сто",
        2: "Двести",
        3: "Триста",
        4: "Четыреста",
        5: "Пятьсот",
        6: "Шестьсот",
        7: "Семьсот",
        8: "Восьмисот",
        9: "Девятьсот"
    }
    return switcher.get(argument, "Invalid")

def dozens(argument):
    switcher = {
        0: "",
        1: "Десять",
        2: "Двадцать",
        3: "Тридцать",
        4: "Сорок",
        5: "Пятьдесят",
        6: "Шестьдесят",
        7: "Семьдесят",
        8: "Восемьдесят",
        9: "Девяносто",
    }
    return switcher.get(argument, "Invalid")

def mod_dozens(argument):
    switcher = {
        11: "Одинадцать",
        12: "Двенадцать",
        13: "Тринадцать",
        14: "Четырнадцать",
        15: "Пятнадцать",
        16: "Шестнадцать",
        17: "Семнадцать",
        18: "Восемнадцать",
        19: "Девятнадцать"
    }
    return switcher.get(argument, "Invalid")


def units(argument):
    switcher = {
        0: "",
        1: "Один",
        2: "Два",
        3: "Три",
        4: "Четыре",
        5: "Пять",
        6: "Шесть",
        7: "Семь",
        8: "Восемь",
        9: "Девять"
    }
    return switcher.get(argument, "Invalid")

N = int(input("Введите трёхзначное число = \n"))

if (N>99 and N<1000):

    A = int(N/100)
    B = int((N/10)%10)
    C = int(N%10)
    M = int(N%100)

    if (M>10) and (M<20):
        print(hundred(A),mod_dozens(M))
    else:
        print(hundred(A),dozens(B),units(C))
#switch_demo(int(input("Введите от 1 до 12 \n")))
"""
#For5
"""
N = float(input("Введите стоимость конфет за кг = \n"))
assert N>0
for i in range(1,11):
    print("Стоимость за ",float(i/10)," = ", round((float(i/10) *N),2))
"""
#For15
"""
A = float(input("Введите вещественное число = \n"))
N = int(input("Введите целую степень = \n"))
C = 1
for i in range(N):
    C = float(C*A)
assert C>0
print(C)
"""
#While10
"""
N = int(input("Введите целое число = \n"))
K = 1

if N>0:
    while 3 ** K <= N:
        P = 3 ** K
        K = K + 1
    print("Наибольшее число K = \n", K)
"""
#While20
"""
N = int(input("Введите целое число = \n"))
A = 0
assert N>0
if N>0:

    while N>1:
        A = int(N%10)
        N = int(N/10)

        if A == 2:
            print("Имеется число 2")
            break
"""