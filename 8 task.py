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