# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [245 690; 245 756] простые числа. Выведите на экран все найденные простые числа в порядке возрастания, слева от каждого числа выведите его порядковый номер в последовательности. Каждая пара чисел должна быть выведена в отдельной строке.
# Например, в диапазоне [5; 9] ровно два различных натуральных простых числа  — это числа 5 и 7, поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# 1 5
# 3 7

# Импортируем функцию квадратного корня
from math import sqrt
for i in range(121363, 121431):
    # Проверяем, является ли число простым
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            # Число не простое
            break
    else:
        # Цикл не прерывался, множители не найдены
        print('%2d' % (i - 121362), i)

# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [245 690; 245 756] простые числа. Выведите на экран все найденные простые числа в порядке возрастания, слева от каждого числа выведите его порядковый номер в последовательности. Каждая пара чисел должна быть выведена в отдельной строке.
# Например, в диапазоне [5; 9] ровно два различных натуральных простых числа  — это числа 5 и 7, поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# 1 5
# 3 7

a = []
for i in range(245690,245756):
    del_count = 0
    for d in range(2, i):
        if i % d == 0 and i != d:
            del_count += 1

    if del_count == 0:
        a.append(i)

a = sorted(a)

print(a)
for i in range(0, len(a)):
    print(a[i]-245689)


# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [210 235; 210 300], числа, имеющие ровно четыре различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки. Делители в строке должны следовать в порядке возрастания.
# Например, в диапазоне [10; 16] ровно четыре различных натуральных делителя имеет число 12, поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# 2 3 4 6

 

for j in range(210235, 210301):
   count = []
   for i in range(2, j // 2 + 1):
       if j % i == 0:
           count.append(i)
           if len(count) > 4:
               break
   if len(count) == 4:
       print(" ".join(str(s) for s in count))

# Задание 25 № 27855 Добавить в вариант
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [95632; 95700], числа, имеющие ровно шесть различных чётных натуральных делителей (при этом количество нечётных делителей может быть любым). Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки. Делители в строке должны следовать в порядке возрастания.
# Например, в диапазоне [2; 48] ровно шесть чётных различных натуральных делителей имеют числа 24, 36 и 40, поэтому для этого диапазона вывод на экране должна содержать следующие значения:

for j in range(95632, 95701):
   count = []
   for i in range(2, j+1):
       if i % 2 == 0 and j % i == 0:
           count.append(i)
           if len(count) > 6:
               break
   if len(count) == 6:
       print(" ".join(str(s) for s in count))

# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [312614;312651],
# числа, имеющие ровно шесть различных натуральных делителей. Для каждого найденного числа запишите
# эти шесть делителей в шесть соседних столбцов на экране с новой строки. Делители в строке должны
# следовать в порядке возрастания.


for j in range(312614, 312652):
   count = []
   for i in range(1, j+1):
       if j % i == 0:
           count.append(i)
           if len(count) > 6:
               break
   if len(count) == 6:
       print(" ".join(str(s) for s in count))


for x in range(26600,28101):
    k = 0
    for i in range(2,x//2+1):
        if x % i == 0:
            k += 1
    if k % 13 == 0 and k != 0:
        print(x,k)



# 25. Напишите программу, которая ищет среди целых чисел, принадлежа­ щих числовому отрезку [64930; 65050], числа, имеющие ровно три таких разлйчных натуральных делителя, которые кратны и трём, и двум (не счи­ тая самого числа). Для каждого найденного числа запишите: само число на экране, затем три делителя в трёх соседних столбцах на экране, каждое число и его делители с новой строки. Делители в строке таблицы должны следовать в порядке возрастания.
# Например, в диапазоне [85; 93] ровно три (не считая самого чисЛа) раз­ личных натуральных делителя, которые кратны и трём, и двум, имеет чис­ ло 90, поэтому для этого диапазона таблица на экране должна содержать следующие значения:

for j in range(64930,65051):
   count = []
   for i in range(2, j // 2 + 1):
       if j % i == 0 and i % 2 == 0 and i % 3 == 0:
           count.append(i)
           if len(count) > 3:
               break
   if len(count) == 3:
       print(j," ".join(str(s) for s in count))



# 25. Напишите программу, которая ищет среди целых чисел, принадлежа­ щих числовому отрезку [123040; 123080], числа, имеющие ровно три раз­ личных чётных натуральных делителя (не считая самого числа) и сколько угодно нечётных. Для каждого найденного числа запишите сначала само это число, затем три делителя в соседних трёх столбцах на экране с новой строки. Делители в строке таблицы должны следовать в порядке возрас­ тания.
# Например, в диапазоне [25; 31] ровно три целых различных чётных на­ туральных делителя имеют числа 28 и 30, поэтому для этого диапазона таблица на экране должна содержать следующие значения:

for j in range(123040, 123081):
   count = []
   for i in range(2, j//2+1):
       if i % 2 == 0 and j % i == 0:
           count.append(i)
           if len(count) > 3:
               break
   if len(count) == 3:
       print(j," ".join(str(s) for s in count))

# решение на поиск простых чисел

def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
i = 1
for x in range(245690,245756+1):
    if is_prime(x) == True:
        print(i, x, is_prime(x))
    i += 1
            
# решение на поиск кол-ва делителей и вывод самих делителей

def divisors(x):
    k = 0
    for i in range(1,x+1):
        if x % i == 0:
            k += 1
    return k

def divisors_list(x):
    digits = []
    for i in range(1,x+1):
        if x % i == 0:
            digits.append(i)
    return digits

for g in range(185311,185330+1):
    if divisors(g) == 4:
        print(divisors_list(g))
# оптимизированный 
 
def divisors_list(x):
    digits = []
    for i in range(1,x+1):
        if x % i == 0:
            digits.append(i)
    return digits

for g in range(185311,185330+1):
    if len(divisors_list(g)) == 4:
        print(divisors_list(g))
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457; 174505], числа, имеющие ровно два различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа запишите эти два делителя в два соседних столбца на экране с новой строки в порядке возрастания произведения этих двух делителей. Делители в строке также должны следовать в порядке возрастания.

# Например, в диапазоне [5; 9] ровно два различных натуральных делителя имеют числа 6 и 8, поэтому для этого диапазона вывод на экране должна содержать следующие значения:

def divisors(x):
    digits = []
    for i in range(2, x):
        if x % i == 0:
            digits.append(i)
    return digits

for x in range(174457,174505):
    if len(divisors(x)) == 2:
        print(divisors(x))


# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [120115; 120200],
# число, имеющее максимальное количество различных натуральных делителей, если таких чисел несколько — найдите максимальное из них. Выведите на экран количество делителей такого числа и само число.
# Например, в диапазоне [80; 90] максимальное количество различных натуральных делителей имеет число 90,
# поэтому для этого диапазона вывод на экране должна содержать следующие значения:

def divisors(x): # создается функция, которая отбирает натуральные делители
    k = 0 # счетчик
    for i in range(1, x+1): # перебор от первого до самого числа
        if x % i == 0: # проверка деления
            k += 1
    return k

maxDel = divisors(84130) # максимальное количество делитей
max = 84130 # самый большой натуральный делитель
for i in range(84052,84130): # перебор чисел
    k = divisors(i) # в переменную записываются все возможные делители
    if k >= maxDel: # если количество делителей числа больше, чем найденное ранее количество делителей
        max = i # запоминаем количество делителей
        maxDel = k # запоминаем число
print(maxDel,max)


def divisors(x):
    digits = []
    for i in range(2,x):
        if x % i == 0:
            digits.append(i)
    return digits

for i in range(452021,1000000000):
    dels = divisors(i)
    M = max(dels) + min(dels)
    if M % 7 == 3:
        print(i,M)


def divisors(x):
    dels = []
    i = 2
    while i ** 2 < x:
        if x % i == 0:
            dels.append(i)
            dels.append(x // i)
        i += 1
    if x % i == 0:
        dels.append(i)
    dels.sort()
    return dels



for x in range(289123456, 389123456 + 1):
    k = divisors(x)
    if k == 3:
        print(x,max(k))