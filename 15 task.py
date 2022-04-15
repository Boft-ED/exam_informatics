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
