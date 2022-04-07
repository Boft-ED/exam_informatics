def alg(N):
    N = bin(N)[2:]

    if int(N, 2) % 2 == 0:
        N = "1" + N + "0"
    else:
        N = "11" + N + "00"

    return int(N, 2)


for N in range(1, 1000):
    if alg(N) > 52:
        print(N)
        break

# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему
# новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда по следующему
# правилу:
# a) складываются все цифры двоичной записи числа N, и остаток от деления
# суммы на 2 дописывается в конец числа (справа).
# Например, запись 11100 преобразуется в запись 111001;
# б) над этой записью производятся те же действия - справа дописывается
# остаток от деления суммы её цифр на 2.
# Полученная таким образом запись (в ней на два разряда больше, чем
# в записи исходного числа N) является двоичной записью результирующего
# числа R.
# Укажите такое наименьшее число N, для которого результат работы
# данного алгоритма больше числа 77. В ответе это число запишите
# в десятичной системе счисления.

for n in range (30):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + '00'
    else:
        r = r + '10'
    print(n, int(r, 2))


# На вход алгоритма подаётся натуральное
# число N. Алгоритм строит по нему новое число
# R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописывается (дублируется)
# последняя цифра.
# 3. Затем справа дописывается бит чётности:
# О, если в двоичном коде полученного числа
# чётное число единиц, и 1, если нечётное.
# 4. К полученному результату дописывается
# ещё один бит чётности.
# Полученная таким образом запись (в ней на
# три разряда больше, чем в записи исходного
# числа N) является двоичной записью
# искомого числа R.
# Укажите минимальное число N, после
# обработки которого автомат получает число,
# большее 97.

for n in range (1, 100):
    r = bin(n)[2::]
    r += r[-1]

    if r.count('1') % 2 ==0:
        r += '0'
    else:
        r += '1'
    if r.count('1') % 2 ==0:
        r += '0'
    else:
        r += '1'
    r = int(r, 2)

    if r > 97:
        print(n)
        break

# На вход алгоритма подаётся натуральное
# число N. Алгоритм строит по нему новое число
# R следующим образом.
# 1) Строится двоичная запись числа N.
# 2) Затем справа дописываются два разряда:
# символы 01, если число N чётное, и 10, если
# нечётное.
# Полученная таким образом запись (в ней на
# три разряда больше, чем в записи исходного
# числа N) является двоичной записью
# искомого числа R.
# Укажите минимальное число R, большее 130,
# которое может являться результатом работы
# этого алгоритма.

for n in range (1, 100):
    r = bin(n)[2::]

    if r[-1] == '0':
        r += '01'
    else:
        r += '10'

    r = int(r, 2)

    if r > 130:
        print(r)
        break

# На вход алгоритма подаётся натуральное
# число N. Алгоритм строит по нему новое число
# R следующим образом.
# 1) Строится двоичная запись числа N.
# 2) Подсчитывается количество нулей и единиц
# в полученной записи. Если их количество
# одинаково, в конец записи добавляется её
# последняя цифра. В противном случае в конец
# записи добавляется цифра, которая
# встречается реже.
# 3) Шаг 2 повторяется ещё два раза.
# 4) Результат переводится в десятичную
# систему счисления.
# При каком наибольшем исходном числе N <
# 100 в результате работы алгоритма получится
# чётное число, которое не делится на 4?

for n in range (1, 100):
    r = bin(n)[2::]

    if r.count('0') == r.count('1'):
        r += r[-1]
    else:
        if r.count('0') < r.count('1'):
            r += '0'
        else:
            r += '1'

    if r.count('0') == r.count('1'):
        r += r[-1]
    else:
        if r.count('0') < r.count('1'):
            r += '0'
        else:
            r += '1'

    if r.count('0') == r.count('1'):
        r += r[-1]
    else:
        if r.count('0') < r.count('1'):
            r += '0'
        else:
            r += '1'

    r = int(r, 2)

    if r % 2 == 0 and r % 4 != 0:
        print(n)

# Автомат обрабатывает натуральное число N по следующему алгоритму.
# 1. Строится двоичная запись числа N.
# 2. Если N четное, то в конец полученной записи (справа) дописывается 0, в
# начало - 1; если N- нечётное в конец и начало дописывается по две единицы.
# 3. Результат переводится в десятичную систему и выводится на экран.
# Пример. Дано число N= 13. Алгоритм работает следующим образом:
# 1. Двоичная запись числа N: 1101.
# 2. Число нечетное, следовательно по две единицы по краям - 11110111.
# 3. На экран выводится число 247.
# Укажите наименьшее число, большее 52, которое может является результатом
# работы автомата.

def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = '1' + n + '0'
    else:
        n = '11' + n + '11'
    return int(n, 2)

N = 1
m = 100000000
while True:
    if f(N) > 52:
        m = min(m, f(N))
        print(m)
    N += 1


# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) складываются все цифры двоичной записи числа N, и остаток от деления суммы на 2 дописывается в конец числа (справа). Например, запись 11100 преобразуется в запись 111001;
# б) над этой записью производятся те же действия — справа дописывается остаток от деления суммы её цифр на 2.
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R. Укажите минимальное число R, которое превышает число 97 и может являться результатом работы данного алгоритма. В ответе это число запишите в десятичной системе счисления.

def f(N):
    n = bin(N)[2:]
    n += str(sum(map(int, n)) % 2)
    n += str(sum(map(int, n)) % 2)
    return int(n, 2)

N = 1
m = 100000000
while True:
    if f(N) > 97:
        m = min(m, f(N))
        print(m)
    N += 1

# Автомат обрабатывает натуральное число N по следующему алгоритму.
# 1. Строится двоичная запись числа N.
# 2. Если N четное, то в конец полученной записи (справа) дописывается 0, в начало — 1; если N — нечётное в конец и начало дописывается по две единицы.
# 3. Результат переводится в десятичную систему и выводится на экран.
# Пример. Дано число N = 13. Алгоритм работает следующим образом:
# 1. Двоичная запись числа N: 1101.
# 2. Число нечетное, следовательно, по две единицы по краям — 11110111.
# 3. На экран выводится число 247.
# Укажите наименьшее число, большее 52, которое может является результатом работы автомата.

def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = '1' + n + '0'
    else:
        n = '11' + n + '00'
    return int(n, 2)

N = 1
m = 100000000
while True:
    if f(N) > 52:
        m = min(m, f(N))
        print(m)
    N += 1


def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n += '10'
    else:
        n = '1' + n + '01'
    return int(n, 2)

N = 1
while True:
    if f(N) > 516:
        print(N)
        break
    N += 1


# Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
# 1. Строится двоичная запись числа N.
# 2. Вместо последней (самой правой) двоичной цифры дважды записывается вторая слева цифра двоичной записи.
# 3. Результат переводится в десятичную систему.
# Пример. Дано число N = 19. Алгоритм работает следующим образом:
# 1. Двоичная запись числа N: 10011.
# 2. Вторая слева цифра 0, единица в конце записи заменяется на два нуля, новая запись 100100.
# 3. Результат работы алгоритма R = 36.
# При каком наименьшем числе N в результате работы алгоритма получится R > 76? В ответе запишите это число в десятичной системе счисления.

def f(N):
    n = bin(N)[2:-1]
    n += n[1] + n[1]
    return int(n, 2)
N = 4 # увеличивать до получения ответа
while True:
    if f(N) > 76:
        print(N)
        break
    N += 1
Автомат обрабатывает натуральное число N по следующему алгоритму:

# 1. Строится двоичная запись числа N.
# 2. Запись «переворачивается», то есть читается справа налево. Если при этом появляются ведущие нули, они отбрасываются.
# 3. Полученное число переводится в десятичную запись и выводится на экран.
# Пример. Дано число N = 58. Алгоритм работает следующим образом.
# 1. Двоичная запись числа N: 111010.
# 2. Запись справа налево: 10111 (ведущий ноль отброшен).
# 3. На экран выводится десятичное значение полученного числа 23.
# Какое наибольшее число, не превышающее 100, после обработки автоматом даёт результат 13?

def f(N):
    n = bin(N)[2:]
    n = n[::-1]
    return int(n, 2)

for N in range(1, 101):
    if f(N) == 13:
        print(N)

# Алгоритм получает на вход натуральное число N> 1 и строит по нему новое
# число R следующим образом:
# 1.
# Строится двоичная запись числа N.
# 2.
# Вычисляется количество единиц, стоящих на чётных местах в двоичной
# записи числа N без ведущих нулей, и количество нулей, стоящих на нечётных
# местах. Места отсчитываются слева направо (от старших разрядов
# к младшим, начиная с единицы).
# 3. Результатом работы алгоритма становится модуль разности полученных
# двух чисел.
# Пример. Дано число N = 39. Алгоритм работает следующим образом:
# 1. Строится двоичная запись: 3910 = 1001112.
# 2. Выделяем единицы на чётных и нули на нечётных местах: 100111.
# На чётных местах стоят две единицы, на нечётных - один ноль.
# 3. Модуль разности равен 1.
# Результат работы алгоритма R = 1.
# При каком наименьшем N в результате работы алгоритма получится R = 5?

n = 2
while True:
    k0 = k1 = 0
    t = bin(n)[2:]
    for i in range(1, len(t), 2):
        if t[i] == '1':
            k1 += 1
    for i in range(0, len(t), 2):
        if t[i] == '0':
            k0 += 1
    r = abs(k1 - k0)
    if r == 5:
        print(n)
        break
    n += 1

# Алгоритм получает на вход натуральное число N> 1 и строит по нему новое число R
# следующим образом:
# 1. Вычисляется сумма чётных цифр в десятичной записи числа N. Если чётных
# цифр в записи нет, сумма считается равной нулю.
# 2. Вычисляется сумма цифр, стоящих на чётных местах в десятичной записи числа
# N без ведущих нулей. Места отсчитываются слева направо (от старших разрядов к
# младшим, начиная с единицы). Если число однозначное (цифр на чётных местах нет),
# т),
# сумма считается равной нулю.
# 3. Результатом работы алгоритма становится модуль разности полученных двух
# При каком наименьшем N в результате работы алгоритма получится R = 13?

def f(N):
    s1 = 0
    N = str(N)
    for i in range(len(N)):
        if int(N[i]) % 2 == 0:
            s1 += int(N[i])
    s2 = 0
    for i in range(len(N)):
        if i % 2 != 0:
            s2 += int(N[i])
    return abs(s1 - s2)

N = 1
while True:
    if f(N) == 13:
        print(N)
        break
    N += 1


# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1. Строится двоичная запись числа N.
# 2. В конец записи (справа) добавляется (дублируется) последняя цифра.
# 3. Складываются все цифры полученной двоичной записи. В конец записи (справа) дописывается остаток от деления суммы на 2.
# 4. Результат переводится в десятичную систему и выводится на экран.
# Пример. Дано число N = 13. Алгоритм работает следующим образом:
# 1. Двоичная запись числа N: 1101.
# 2. Дублируется последняя цифра, новая запись 11011.
# 3. Сумма цифр полученной записи 4, остаток от деления на 2 равен 0, новая запись 110110.
# 4. На экран выводится число 54.
# Какое наименьшее число, большее 105, может появиться на экране в результате работы автомата?

def f(N):
    n = bin(N)[2:]
    n += n[-1]
    n += str(sum(map(int, n)) % 2)
    return int(n, 2)

N = 1
m = 1000000

while True:
    if f(N) > 105:
        m = min(m, f(N))
        print(m)
    N += 1


# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё несколько разрядов по следующему правилу:
# a) Если N чётное, то к нему справа приписывается в двоичном виде сумма цифр его двоичной записи;
# б) Если N нечётное, то к нему справа приписываются два нуля, а слева единица.
# Полученная таким образом запись (в ней как минимум на один разряд больше, чем в записи исходного числа N) является
# двоичной записью искомого числа R.
# Например, запись числа 1101 будет преобразована в 1110100.
# Укажите такое наименьшее число N, для которого результат работы данного алгоритма больше числа 215. В ответе это
# число запишите в десятичной системе счисления.

n = 1

while True:
    x = bin(n)[2:]
    if x[-1] == '0':
        x += bin(x.count('1'))[2:]
    else:
        x = '1' + x + '00'
    r = int(x, 2)
    if r > 215:
        print(n)
        break
    n += 1

def alg(N):
    if N % 2 == 0:
        N = bin(N)[2:] + "01"
    else:
        N = bin(N)[2:] + "10"

    return int(N, 2)


a = []
for i in range(1, 100000):
    t = alg(i)
    if t > 81:
        a.append(t)
print(min(a))