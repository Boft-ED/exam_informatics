from itertools import *


def f(x, A):
    return x % A == 0


A = 1

while True:
    for x in range(1, 10000000):
        if not ((not f(x, A)) <= (f(x, 3) <= (not f(x, 5)))):
            break
    else:
        print(A)
    A += 1

# делимость ДЕЛ
for a in range(1, 1000):
    flaq = 1
    for x in range(1, 10000):
        f = (a % 9 == 0) and ((280 % x == 0) <=
                              ((a % x != 0) <= (730 % x != 0)))
        if f == 0:
            flaq = 0
            break
    if flaq == 1:
        print(a)

for a in range(1, 1000):
    for x in range(1, 10000):
        f = ((x % 34 == 0) and (x % 51 != 0)) <= (
            (x % a != 0) or (x % 51 == 0))
        if f == 0:
            break
    else:
        print(a)


def f(x):
    return ((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)


for a in range(1, 10000):
    if all(f(x) == 1 for x in range(1, 100000)):
        print(a)

# конъюнкция &


def f(x):
    return (x & 41 == 0) <= ((x & 119 != 0) <= (x & a != 0))


for a in range(1, 100):
    if all(f(x) == 1 for x in range(1, 10000)):
        print(a)


def f(x):
    return (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))


for a in range(1, 100):
    if all(f(x) == 1 for x in range(1, 10000)):
        print(a)


def f(x):
    return (x & a == 0) and (x & 41 != 0) and (x & 33 == 0)


for a in range(1, 1000):
    if all(f(x) == 0 for x in range(1, 10000)):
        print(a)


def f(x):
    b = ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0)))
    c = ((x & 8 == 0) and (x & a != 0) and (x & 58 == 0))
    return b <= c


for a in range(43, 56):
    if all(f(x) == 0 for x in range(1, 10000)):
        print(a)

# числовая плоскость


def f(x, y):
    return (y + 3 * x < a) or (x > 20) or (y > 40)


for a in range(1, 10000):
    if all(f(x, y) == 1 for x in range(1, 100) for y in range(1, 100)):
        print(a)


def f(x, y):
    return (2*y + 3*x < a) or (x+y > 40)


for a in range(1, 200):
    if all(f(x, y) == 1 for x in range(0, 100) for y in range(0, 100)):  # целых неотрицатльных чисел
        print(a)


def f(x, y, z):
    return (220 != y + 2*x + z) or (a < 6 * x) or (a < y) or (a < 2*z)


for a in range(1, 200):
    if all(f(x, y, z) == 1 for x in range(0, 150) for y in range(0, 150) for z in range(0, 150)):
        print(a)

# сколько существует комбинаций
k = 0
for x in range(0, 100):
    for y in range(0, 100):
        f = not(((x > 6) and ((x + y) >= 5)) or (y >= 5))
        if f == 1:
            k += 1
print(k)

# множества

# поиск минимального значения
a = set()
b = {2, 4, 6, 8, 10, 12}
c = {3, 6, 9, 12, 15}


def f(x):
    A = x in a
    B = x in b
    C = x in c
    return B <= ((C and (not A)) <= (not B))


for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(a)


a = set()
b = {2, 4, 6, 8, 12}
c = {3, 9, 12, 15}


def f(x):
    A = x in a
    B = x in b
    C = x in c
    return (not B) or ((not C) <= A)


for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(a)  # ответ 640 т.к произвдение минимальных

# поиск максимального значения

a = set(range(1000))
p = {2, 4, 6, 8, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}


def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) and (Q <= (not A))


for x in range(1000):
    if f(x) == 0:
        a.remove(x)
print(a)  # ответ 18


# отрезки

from itertools import *

def f(x):
    P = 25 <= x <= 50
    Q = 54 <= x <= 75
    A = a1 <= x <= a2
    return Q <= ((not P) == Q and ((not P) <= A))


Ox = [i/4 for i in range(24*4, 76*4)]
m = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2-a1)
print(min(m))


from itertools import *

def f(x):
    P = 25 <= x <= 37
    Q = 32 <= x <= 50
    A = a1 <= x <= a2
    return (A and (not Q)) <= (P or Q)

m = []
Ox = [i/4 for i in range(25*4,51*4)]

for a1,a2 in combinations(Ox,2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2-a1)
print(max(m))


from itertools import *

def f(x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = a1 <= x <= a2
    return (P == Q) <= (not A)

Ox = [i/4 for i in range(4*4,24*4)]
m = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2-a1)
print(max(m)) # ответ 9