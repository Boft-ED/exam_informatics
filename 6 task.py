# Определите, при каком наибольшем введённом значении переменной s
# программа выведет число 64. Для Вашего удобства программа представлена
# на четырёх языках программирования.

for i in range(1, 10000):
    s = i
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        print(i)

# Задание 22 № 9204  Ниже на пяти языках записан алгоритм. Получив на вход число x, этот алгоритм печатает два числа a и b. Укажите наименьшее из таких чисел x, при вводе которых алгоритм печатает сначала 2, а потом 11.

for i in range(1, 10000): # если нужно найти наибольшее, то for i in range(10000000, 1, -1): 
    x = i
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 1000)
        x = x // 1000
    if a == 2 and b == 11:
        print(i)

# # (Е. Джобс) Определите, сколько существует целых положительных значений, подаваемых на вход программе, при которых программа выведет 80.
# s = int(input())
# n = 10
# while s - n < 1000:
#     s = s + n
#     n = n + 5
# print(n)

count = 0
for i in range(1, 1010):
    s = i
    n = 10
    while s - n < 1000:
        s = s + n
        n = n + 5
    if n == 80:
        count += 1
print(count)


def f(x):
    L = x
    M = 132
    if L % 2 != 0:
        M = 64
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    return M

x = 1
while True:
    if f(x) < 480 and f(x) == 12:
        print(x)
        break
    x += 1



count = 0
for i in range(1, 1010):
    s = i
    x = i
    s = 100 * s + x
    n = 1
    while s < 2021:
        s = s + 5 * n
        n = n + 1
    if n == 15:
        count += 1
print(count)


count = 0
for i in range(1019, 100000, 1019):
    for j in range(1019, 100000, 1019):
        x = i
        y = j
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        if x == 1019:
            count += 1
print(count)