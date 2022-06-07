a = [int(x) for x in open('27-A_2.txt')]

ans = []
n = len(a)

for i in range(n-1):
    for k in range(i+1, n):
        if (a[i] * a[k]) % 14 == 0:
            ans.append(a[i] * a[k])
print(max(ans))

a = [int(x) for x in open('27-B_2.txt')]

ans = []
n = len(a)

for i in range(n-1):
    for k in range(i+1, n):
        if (a[i] * a[k]) % 14 == 0:
            ans.append(a[i] * a[k])
print(max(ans))

a,b = map(int,input().split())
print(a,b)