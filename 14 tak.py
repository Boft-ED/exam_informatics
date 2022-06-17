def convert(x, n):
    digits = ""
    while x:
        digits += str(x % n)
        x //= n
    return digits[:: -1]


a = 49  7 + 7  20 - 28

print(convert(a, 7).count("6"))

x = 2197 ** 50 - 169 ** 35 - 26
k = 0
while x > 0:
    if x % 13 == 12:
        k += 1
    x //= 13
print(k)

x = 1
while True:
    a = 64 ** 12 - 8 ** 14 + x
    s = ''
    while a != 0:
        s = str(a % 8) + s
        a //= 8
    if s.count('7') == 12 and s.count('1') == 1:
        print(x)
        break
    x += 1

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


# Значение выражения 2435 + З7 - 2 - X записали в системе счис­ ления с основанием 3, при этом в записи оказалось ровно 20 цифр «2». При каком минимальном целом положительном X это возможно?

x = 1
while True:
    a = 243 ** 5 + 3 ** 7 - 2 - x
    s = ''
    while a != 0:
        s = str(a % 3) + s
        a //= 3
    if s.count('2') == 20:
        print(x)
        break
    x += 1

# Сколько различных цифр содержится в этой записи?

x = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18388
d = set()
while x > 0:
    d.add(x % 15)
    x = x // 15
print(len(d))

# записали в системе счисления с основанием 6. Определите сумму цифр в записи этого числа.

x =
s = 0
while x > 0:
    s += x % 6
    x = x//6
print(s)