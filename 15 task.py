def f(x, A):
    return x % A == 0

A = 1

while True:
    for x in range(1, 10000000):
        if not ((not f(x, A)) <= (f(x,3) <= (not f(x, 5)))):
            break
    else:
        print(A)
    A += 1