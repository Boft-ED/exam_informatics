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