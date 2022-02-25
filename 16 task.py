def F(n):
    if n == 1:
        return 3
    if n > 1:
        return F(n-1) * (n-1)

print(F(6))    

def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) + 1
    if n >= 2 and (not (n % 3 == 0)):
        return f(n - 2) + 5
k = 0
for n in range(1,100000):
    if f(n) == 55:
        k += 1
print(k)