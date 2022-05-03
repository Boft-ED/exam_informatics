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

# (А. Куканова) Катя составляет трёхбуквенные слова из букв А, Б, В, Г, Д, причём буквы могут повторяться, но следуют друг за другом в алфавитном порядке. Сколько различных слов может составить Катя?

from itertools import product
words = list(product('АБВГД', repeat=3))
word = list(map("".join,words))

k = 0
for x in range(len(word)):
    if word[x][1] >= word[x][0]:
        if word[x][2] >= word[x][1]:
            k += 1x
print(k)

# 8. Борис составляет четырёхбуквенные слова, в которых есть только бук­ вы Е, Д, О, Н и К, причём в каждом слове буква О используется ров­ но 2 раза. Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем. Словом считается лю­ бая допустимая последовательность букв, необязательно осмысленная. Сколько слов может составить Борис?


from itertools import product
words = list(product('ЕДОНК', repeat=4))
word = list(map("".join,words))

k = 0
for x in range(len(word)):
    if word[x].count('О') == 2:
        k += 1
print(k)

# Саша составляет слова, переставляя буквы из слова «ИДИЛЛИЯ». Словом считается любая допустимая последовательность букв, не обяза­
# тельно осмысленная.
# Сколько существует различных слов, которые может написать Саша?

from itertools import permutations
s = 'ИДИЛЛИЯ'
res = set()
for comb in permutations(s):
    res.add(''.join(comb))
print(len(res))


# Петя составляет слова из слова ПАРУС и записывает их в алфавитном порядке в список. Вот начало списка 
# Под каким номером идет первое слово в списке, начинающегося на  У, в котором две буквы А не стоят рядом?

from itertools import product
words = list(product('АПРСУ', repeat=5))
k = 0

for x in words:
    k += 1
    x = ''.join(x)
    if x[0] == 'У' and 'АА' not in x:
        print(k)
        print(x)
        break

# Определите количество пятизначных чисел, записанных в десятичной системе счисления, учитывая, что числа не могут заканчиваться на цифры 3, 4 и 7 и не должны содержать тройки соседних одинаковых цифр (например, 000).

from itertools import product
k = 0

for x in product('0123456789',repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s[-1] not in '347':
        if all(d * 3 not in s for d in '0123456789'):
            k += 1
print(k)

# Определите количество семизначных чисел, записанных в девятеричной системе счисления, учитывая, что числа не могут начинаться с цифр 3 и 7 и не должны содержать пары соседних одинаковых цифр (например, 00).

from itertools import product
k = 0

for x in product('012345678',repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s[0] not in '37':
        if all(d * 2 not in s for d in '012345678'):
            k += 1
print(k)


# согласные в конце и гласные в начале 

from itertools import product
k = 0
for x in product('КУМА', repeat=5):
    s = ''.join(x)
    if s[0] in 'КМ' and s[-1] in 'УА':
        k += 1
print(k)

# буква О повторяется ровно 1 раз 

from itertools import product

k = 0
for x in product('КРОТ', repeat=6):
    s = ''.join(x)
    if s.count('О') == 1:
        k += 1
print(k)

# буква E повторяется хотя бы 1 раз 

from itertools import product

k = 0
for x in product('ЛЕТО', repeat=4):
    s = ''.join(x)
    if s.count('Е') >= 1:
        k += 1
print(k)

# ровно 1 бука Ж и не может начинаться на Ф и заканччиваться на Р
from itertools import product

k = 0
for x in product('ЖИРАФ', repeat=5):
    s = ''.join(x)
    if s.count('Ж') == 1 and s[0] != 'Ф' and s[-1] != 'Р':
        k += 1
print(k)

# перестановки

from itertools import permutations

k = 0
for x in set(permutations('АССАСИН')):
    k += 1
print(k)


from itertools import permutations

k = 0
for x in permutations('КАЛИЙ'):
    s = ''.join(x)
    if s[0] != 'Й' and 'ИА' not in s:
        k += 1
print(k)

# Ь не может стоять на первом месте и перед буквами АЕР

from itertools import permutations

k = 0
for x in permutations('ПЕСКАРЬ'):
    s = ''.join(x)
    if s[0] != 'Ь' and 'ЬА' not in s and 'ЬЕ' not in s and 'ЬР' not in s:
        k += 1
print(k)

# числа N делящихся на 4 без остатка
from itertools import product

k = 0

for x in product('01234567',repeat=4):
    s = ''.join(x)
    if s[0] != '0' and s[-1] in '04':
        k += 1
print(k)


# порыдок невозрастания 

from itertools import product

k = 0

for x in product('01234567',repeat=4):
    s = ''.join(x)
    if s[0] >= s[1] >= s[2] >= s[3]:
        k += 1
print(k)


# две соседние цифры различны 
from itertools import product

k = 0

for x in product('01234567',repeat=5):
    s = ''.join(x)
    if s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
        k += 1
print(k)


# перебор слов 
from itertools import product
k = 0
for x in product('АКРУ', repeat=5):
    k += 1
    s = ''.join(x)

    if k == 150:
        print(s)


from itertools import product
k = 0
for x in product('АОУ', repeat=5):
    k += 1
    s = ''.join(x)

    if s == "УАУАУ":
        print(k,s)


from itertools import product
k = 0
for x in product('АПРСУ',repeat=5):
    k += 1
    s = ''.join(x)
    if s[0] == 'У' and 'АА' not in s:
        print(k,s)