# В файле 17-4.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от 0 до 10
# О00 включительно. Рассматривается множество элементов
# Les
# последовательности, которые удовлетворяют следующим условиям:
# - в числе есть хотя бы два нуля;
# - число кратно 7.
# Найдите наибольшее из таких чисел и их количество.
f = open('17-4.txt', 'r')
s = [int(x) for x in f]
f.close()
res = []
for i in s:
    if str(i).count('0') >= 2 and i % 7 == 0:
        res.append(i)
print(max(res), len(res))


# В файле 17-205.txt содержится последовательность целых чисел. Элементы
# последовательности могут принимать целые значения от -10 000 до 10 000
# включительно. Определите количество пар, в которых хотя бы один из двух
# элементов заканчивается на 7, а их сумма делится на 12. В ответе запишите
# два числа: сначала количество найденных пар, а затем - максимальную
# сумму элементов таких пар. В данной задаче под парой подразумевается два
# идущих подряд элемента последовательности.
f = open('17-205.txt', 'r')
s = [int(x) for x in f]
f.close()
res = []
for i in range(1, len(s)):
    if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 == 7) and (s[i] + s[i-1]) % 12 == 0:
        res.append(s[i] + s[i-1])
print(len(res), max(res))

# В файле 17-243.txt содержится последовательность целых чисел. Элементы
# последовательности могут принимать целые значения от 0 до 10 000
# включительно. Определите количество пар чисел, в которых ровно один из
# двух элементов больше, чем сумма цифр всех чисел в файле, делящихся на
# 61, а десятичная запись другого оканчивается на 33. В ответе запишите два
# числа: сначала количество найденных пар, а затем - минимальную сумму
# элементов таких пар. В данной задаче под парой подразумевается два
# идущих подряд элемента последовательности.

f = open('17-243.txt', 'r')
s = [int(x) for x in f]
f.close()
res = []
summa = 0
for i in s:
    if i % 61 == 0:
        summa += sum(map(int, str(i)))
for i in range(1, len(s)):
    if (s[i-1] > summa and not(s[i] > summa) and str(s[i])[-2:] == '33') or \
            (s[i] > summa and not(s[i-1] > summa) and str(s[i-1])[-2:] == '33'):
        res.append(s[i] + s[i-1])
print(len(res), min(res))

# В файле содержится последовательность из 10 000 целых положительных
# чисел. Каждое число не превышает 10 000. Определите и запишите в ответе
# сначала количество пар элементов последовательности, разность которых
# четна и хотя бы одно из чисел делится на 19, затем максимальную из сумм
# элементов таких пар. В данной задаче под парой подразумевается два
# различных элемента последовательности. Порядок элементов в паре не важен.
# 17.txt
f = open('17.txt', 'r')
s = [int(x) for x in f]
f.close()
res = []
for i in range(0, len(s)-1):
    for j in range(i+1, len(s)):
        if ((s[i] - s[j]) % 2 == 0) and (s[i] % 19 == 0 or s[j] % 19 == 0):
            res.append(s[i] + s[j])
print(len(res), max(res))

# В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от −10 000 до 10 000 включительно. Определите и запишите в ответе сначала количество пар элементов последовательности, в которых хотя бы одно число делится на 3, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности. Например, для последовательности из пяти элементов: 6; 2; 9; –3; 6 — ответ: 4 11.

f = open('17-2.txt', 'r')
s = [int(x) for x in f]
f.close()

c = 0
mx = -1000000

for i in range(len(s)-1):
    if (s[i]* s[i+1] % 3 == 0):
        c += 1
        mx = max(mx, s[i] + s[i+1])
print(c, mx)