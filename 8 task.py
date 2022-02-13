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
