import itertools


# product - Буквы в коде могут повторяться
# permutations - Буквы в коде не повторяются

def check(arr):
    count = 0
    for k in i:
        if k == "И":
            count += 1

    if count >= 1:
        return True
    else:
        return False


s = "ИВАН"
a = set(itertools.product(s, repeat=5))

count = 0

for i in a:
    if check(i):
        count += 1

print(count)



from itertools import permutations
s = 'ТАРТАР'
res = set()
for comb in permutations(s):
    res.add(''.join(comb))
print(len(res))

1,2,4,6,8,10,12,17,14,

# Светлана составляет коды из букв слова ПАРАБОЛА. Код должен состоять из 8 букв, и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове. Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.

# Сколько кодов может составить Светлана?

s = "ПРБЛ"
g = "АО"
count = 0
for s1 in s:
    for s2 in g:
        for s3 in s:
            for s4 in g:
                for s5 in s:
                    for s6 in g:
                        for s7 in s:
                            for s8 in g:
                                word = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
                                if word.count('П') == 1:
                                    if word.count('А') == 2:
                                        if word.count('Р') == 1:
                                            if word.count('Б') == 1:
                                                if word.count('О') == 2:
                                                    if word.count('Л') == 1:
                                                        count += 1
for s1 in g:
    for s2 in s:
        for s3 in g:
            for s4 in s:
                for s5 in g:
                    for s6 in s:
                        for s7 in g:
                            for s8 in s:
                                word = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
                                if word.count('П') == 1:
                                    if word.count('А') == 2:
                                        if word.count('Р') == 1:
                                            if word.count('Б') == 1:
                                                if word.count('О') == 2:
                                                    if word.count('Л') == 1:
                                                        count += 1
print(count)


from itertools import product
k = 0
words=list(product('AБВГДЕ', repeat=4))
word=list(map("".join, words))

for x in range(len(word)):
    if word[x][0] != word[x][2] and word[x][2] != word[x][3] and word[x][2] != 'E':
        if word[x].count('A') > 0:
            k += 1
print(k)

# Определите количество семизначных чисел, записанных в семеричной системе счисления, учитывая, что числа нем
# начинаться с цифр 3 и 5 и не должны содержать сочетания цифр 22 и 44 одновременно.

alf = '0123456'
count = 0
word = ''
for s1 in alf:
    for s2 in alf:
        for s3 in alf:
            for s4 in alf:
                for s5 in alf:
                    for s6 in alf:
                        for s7 in alf:
                            word = s1 + s2 + s3 + s4 + s5 + s6 + s7
                            if word[0] != '0' and word[0] != '3' and word[0] != '5':
                                if not('22' in word and '44' in word):
                                    count += 1
print(count)

from itertools import product
words = list(product('КОМ', repeat=6))
word = list(map("".join,words))

k = 0
for x in range(len(word)):
    if word[x][3]!='К' and word[x][4]!='К' and word[x][5]!='К':
        if word[x].count('K')<3:
            k+=1
print(k)

# 8. Саша составляет шестибуквенные слова, в которых встречаются толь-
# ко буквы С, О, Н. Причём буква С может стоять только на первом, вто-
# ром или третьем местах и встречаться или только один раз, или ровно три
# раза, или не встречаться вовсе. Қаждая из других допустимых букв мо-
# жет встречаться в слове на любом месте или не встречаться совсем. Сло-
# вом считается любая допустимая последовательность букв, необязатель-
# ＿ но осмысленная. Сколько существует таких слов, которые может напи-
# стать Саша?

from itertools import product
words = list(product('СОН', repeat=6))
word = list(map("".join,words))

k = 0
for x in range(len(word)):
    if word[x][3]!='С' and word[x][4]!='С' and word[x][5]!='С':
        if word[x].count('С')==0 or word[x].count('С')==1 or word[x].count('С')==3:
            k+=1
print(k)