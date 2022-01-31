def F(n):
    if n == 1:
        return 3
    if n > 1:
        return F(n-1) * (n-1)

print(F(6))    