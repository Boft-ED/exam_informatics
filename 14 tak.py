def convert(x, n):
    digits = ""
    while x:
        digits += str(x % n)
        x //= n
    return digits[:: -1]


a = 49  7 + 7  20 - 28

print(convert(a, 7).count("6"))

# Значение выражения 3⋅3438+5⋅4912+715−49 записали в системе счисления с основанием 7 без незначащих нулей. Какая цифра чаще всего встречается в этой записи?

a = 5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 - 98
s = ''
while a != 0:
    s = str(a % 7) + s
    a //= 7
print(0, s.count('0'))
print(1, s.count('1'))
print(2, s.count('2'))
print(3, s.count('3'))
print(4, s.count('4'))
print(5, s.count('5'))
print(6, s.count('6'))
