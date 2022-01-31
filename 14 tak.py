def convert(x, n):
    digits = ""
    while x:
        digits += str(x % n)
        x //= n
    return digits[:: -1]


a = 49  7 + 7  20 - 28

print(convert(a, 7).count("6"))