# на память 
# 8460
a = [int(x) for x in open('27884.txt')]
a.sort()
size = 8460
i = 0
storage = []
while i < len(a):
    storage.append(a[i])
    if sum(storage) > size:
        storage.pop()
        break
    i += 1
print(i)

while i < len(a):
    storage.pop()
    storage.append(a[i])
    if sum(storage) > size:
        storage.pop()
        storage.append(a[i-1])
        break
    i += 1
print(sum(storage))

# на скидки 

a = [500, 30, 40, 100, 50, 80, 1000, 150, 200]
a.sort()
not_sale = []
sale = []
i = 0

while a[0] <= 50:
    not_sale.append(a[0])
    a.remove(a[0])

while i < len(a)//2:
    sale.append(a[i])
    a[i] *= 0.75 # меняется 
    i += 1
print(sum(a)+sum(not_sale),max(sale))


# на память запишите в ответе два числа: сначала наибольшее число пользователей, чьи файлы могут быть помещены в архив, затем максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что сохранены файлы максимально возможного числа пользователей.

a = [int(x) for x in open('26_demo.txt')]
a.sort()
size = 8200
i = 0
storage = []
while i < len(a):
    storage.append(a[i])
    if sum(storage) > size:
        storage.pop()
        break
    i += 1
print(i)

while i < len(a):
    storage.pop()
    storage.append(a[i])
    if sum(storage) > size:
        storage.pop()
        storage.append(a[i-1])
        break
    i += 1
print(max(storage))