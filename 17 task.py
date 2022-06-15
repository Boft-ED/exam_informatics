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

# В файле 17-205.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно. Определите количество пар, в которых хотя бы один из двух элементов заканчивается на 17, а их сумма делится на 2. В ответе запишите два числа: сначала количество найденных пар, а затем – максимальную сумму элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

f = open('17-205.txt', 'r')
s = [int(x) for x in f]
f.close()
res = []
for i in range(1, len(s)):
    if (abs(s[i]) % 100 == 17 or abs(s[i-1]) % 100 == 17) and (s[i] + s[i-1]) % 2 == 0:
        res.append(s[i] + s[i-1])
print(len(res), max(res))

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

# В файле 17-205.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно. Определите количество пар, в которых хотя бы один из двух элементов делится на 7, а их сумма заканчивается на 19. В ответе запишите два числа: сначала количество найденных пар, а затем – максимальную сумму элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

a = list(map(int, open('17-205.txt')))

count = 0
m = -10001

for i in range(len(a) - 1):
    if (a[i] % 7 == 0 or a[i+1] % 7 == 0) and abs(a[i] + a[i+1]) % 100 == 19:
        count += 1
        m = max(m, a[i] + a[i+1])
print(count, m)



with open("17.txt") as f:
    s = f.read().split()

nums = [int(i) for i in s]

a = []
for num in nums:
    if num % 5 == 0 and num % 7 == 0 and num % 2 != 0 and num % 11 != 0 and num % 91 != 0:
        a.append(num)

print(max(a), len(a))


#  В файле содержится последовательность целых чисел. Элементы по­ следовательности могут принимать целые значения от -10000 до 10000 включительно. Определите и запишите сначала количество чисел, кото­ рые делятся нацело на 3, но не делятся нацело на 2, а затем второе по вели­ чине из них в порядке возрастания (следующее за минимумом и отличное от него). Гарантируется, что хотя бы два подходящих числа в последова­ тельности есть. Например, для последовательности из шести элементов:


f = open('17.txt')
a = [int(x) for x in f]
k = 0
max1 = 10000
max2 = 10000

for t in range(len(a)):
    if a[t] % 3 == 0 and a[t] % 2 != 0:
        k += 1
        if a[t] <= max1:
            max2 = max1
            max1 = a[t]
        elif a[t] < max2:
            max2 = a[t]
print(k,max2)


# следовательности могут принимать целые значения от —10000 до 10000 включительно. Определите и запишите в ответе сначала количество пар элементов последовательности, в которых оба числа делятся нацело на 5, затем максимальную из сумм элементов таких пар. Гарантируется, что
# найдётся хотя бы одна такая пара. В данной задаче под парой подразуме­ вается два идущих подряд элемента последовательности. Например, для последовательности из пяти элементов: 6; —5; 45; —10; 6 — ответ:

f = open('17.txt')
a = [int(x) for x in f]
k = 0
maxchr = -100000
for i in range(len(a)):
    if a[i] % 5 == 0 and a[i+1] % 5 == 0:
        k += 1
        maxchr = max(maxchr, a[i] + a[i+1])
print(k,maxchr)




a = [int(x) for x in open('17.txt')]
ans = []
for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] % 7 !=0 and a[i] % 17 !=0  and a[i] % 19 !=0 and a[i] % 27 !=0:
        ans.append(a[i])
print(len(ans),max(ans))



a = [int(x) for x in open('17.txt')]
ans = []

for i in range(len(a)):
    if a[i] % 10 == 3 or a[i] % 10 == 5:
        ans.append(a[i])
print(len(ans),max(ans))



a = [int(x) for x in open('17.txt')]
ans = []

for i in range(len(a)):
    if (a[i] % 16 == 11 or a[i] % 16 == 13) and a[i] % 7 == 0 and a[i] % 6 != 0 and a[i] % 13 != 0 and a[i] % 19 != 0:
        ans.append(a[i])
print(sum(ans),len(ans))



a = [int(x) for x in open('17.txt')]
ans = []
for i in range(len(a)-1):
    if abs(a[i]) % 10 == 7 or abs(a[i]) % 10 == 7:
        ans.append(a[i]+a[i+1])
print(len(ans),max(ans))



a = [int(x) for x in open('17.txt')]
ans = []

for i in range(len(a)-1):
    if (a[i] + a[i+1]) % 3 == 0 and (a[i] + a[i+1]) % 6 != 0 and abs(a[i] * a[i+1]) % 10 == 8:
        ans.append(a[i]+a[i+1])
print(len(ans),max(ans))



a = [int(x) for x in open('17.txt')]
ans = []

for i in range(len(a)-2):
    if (a[i] * a[i+1] * a[i+2]) % 7 == 0 and abs(a[i] + a[i+1] + a[i+2]) % 10 == 5:
        ans.append(a[i] + a[i+1] + a[i+2])
print(len(ans),min(ans))



a = [int(x) for x in open('17.txt')]
ans = []

for i in range(len(a)):
    if oct(a[i])[-1] == '7' and oct(a[i])[-2] == '2':
        ans.append(a[i])
print(len(ans),max(ans))



a = [int(x) for x in open('17.txt')]
ans = []

for i in range(len(a)):
    s = sum(map(int,str(a[i])))
    if s % 3 == 0:
        ans.append(a[i])
print(len(ans),max(ans))



a = [int(x) for x in open('17.txt')]
ans = []
avg = sum(a)/len(a)

for i in range(len(a)-1):
    if a[i] > avg and a[i+1] > avg and abs(a[i] + a[i+1]) % 100 == 31:
        ans.append(a[i]+a[i+1])
print(len(ans),max(ans))



a = [int(x) for x in open('17.txt')]
m = max(x for x in a if x % 119 == 0)

ans = []

for i in range(len(a)-1):
    if (a[i] or a[i+1]) > m and (a[i] % 100 == 21 or a[i+1] % 100 == 21):
        ans.append(a[i] + a[i+1])
print(len(ans),min(ans))



a = [int(x) for x in open('17.txt')]

max = max([x for x in a if x % 2 != 0])
min = min([x for x in a if x % 2 != 0])
ans = []

for i in range(len(a)-1):
    if (a[i] + a[i+1]) % 2 == 0 and a[i] + a[i+1] > max + min:
        ans.append(a[i] + a[i+1])
print(len(ans),max(ans))


a = [int(x) for x in open('17.txt')]

ans = []

for i in range(len(a)):
    for k in range(i, len(a)): # два различных элемента последовательности
        if (a[i] + a[k]) % 2 != 0 and (a[i] * a[k]) % 3 == 0:
            ans.append(a[i] + a[k])
print(len(ans), max(ans))


a = [int(x) for x in open('17.txt')]

ans = []

for i in range(len(a)-1):
    for k in range(i, len(a)): # два различных элемента последовательности
        if (a[i] % 160 != a[k] % 160) and (abs(a[i]) % 7 == 0 or abs(a[k]) % 7 == 0):
            ans.append(a[i]+a[k])
print(len(ans),max(ans))



a = [int(x) for x in open('17.txt')]

ans = []
for i in range(len(a)):
    for k in range(i, len(a)): # два различных элемента последовательности
        if (a[i] + a[k]) % 2 != 0 and (a[i] * a[k]) % 3 == 0:
            ans.append(a[i] + a[k])
print(len(ans),max(ans))


a = [int(x) for x in open('17.txt')]

ans = []

for i in range(len(a)-1):
    if (a[i] + a[i+1]) % 2 == 0 and abs(a[i] + a[i+1]) % 10 != 6:
        ans.append((a[i] + a[i+1])//2)
print(len(ans),max(ans))

#Определите количество пар последовательности, в которых хотя бы одно число кратно минимальному числу в последовательности, кратному 17

a = [int(x) for x in open('17.txt')]
ans = []
min = min([x for x in a if x % 17 == 0])

for x in range(len(a)-1):
    if a[x] % min == 0 or a[x+1] % min == 0:
        ans.append(a[x] + a[x+1])
print(len(ans),max(ans))


# если число отрицательное, то abs(a[i])
# часть условия с союзом или надо брать в скобки (a[i] % 16 == 11 or a[i] % 16 == 13)

a = [int(x) for x in open('17.txt')]

ans = []

n = len(a)

for i in range(n-1):
    for k in range(i+1, n):
        if (a[i] * a[k]) % 14 != 0:
            ans.append(a[i] + a[k])
print(len(ans),max(ans))


a = [int(x) for x in open('17.txt')]

ans = []
n = len(a)

for i in range(n-1):
    for k in range(i+1, n):
        if (a[i] + a[k]) % 2 != 0 and (a[i] * a[k]) % 3 == 0:
            ans.append(a[i] + a[k])
print(len(ans),max(ans))



def divisors_list(x):
    digits = []
    for i in range(2,x):
        if x % i == 0:
            digits.append(i)
    return digits


for x in range(289123456, 389123456 + 1):
    k = divisors_list(x)
    if len(k) == 3:
        print(x,max(k))



#for x in range(289123456, 389123456 + 1):