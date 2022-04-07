# Задание 24 № 27698 Добавить в вариант
# Текстовый файл состоит не более чем из 106 символов L, D и R. Определите длину самой длинной последовательности, состоящей из символов R. Хотя бы один символ R находится в последовательности.

# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('zadanie24_2.txt')
s = f.read()
r = 'R'
while r in s:
    r += 'R'
print(len(r) - 1)


# Задание 24 № 29672 Добавить в вариант
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z). Определите количество строк, в которых буква E встречается чаще, чем буква A.

# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('24-1.txt')
s = f.read()
i = s.split('\n')
result = 0
for line in i:
    if line.count('E') > line.count('A'):
        result += 1
print(result)


f = open('24.txt')
k = 0
maxkol = 0
a = f.read()
for x in range(len(a)-1):
    k = 1
    if a[x] != a[x+1]:
        for i in range(x+2, len(a)-2):
            if a[i] == a[i+1] and a[i] != a[x] != a[x+1]:
                k += 1
            elif a[i+1] != a[i+2] and a[i] != a[i+2]:
                if k > maxkol:
                    maxkol = k
                    break
            else:
                break
print(maxkol)


# Текстовый файл состоит не более чем из 10е символов @, &, # .
# Определите, сколько раз встречается следующее сочетание символов:
# Для выполнения этого задания следует написать программу.

f = open('24.txt')
s = f.read()
k = 0
for i in range(len(s)):
    if (s[i] == '#' and s[i+1] == '@' and s[i+2] == '@'):
        k += 1
print(k)


