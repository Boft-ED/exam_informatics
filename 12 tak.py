b = 1000
c = 0

for i in range(250, 1000):
    s = i * "5"
    while "55555" in s:
      s = s.replace("55555", "88", 1)
      s = s.replace("888", "555", 1)

    if s.count("5") < b:
        b = s.count("5")
        c = i
print(c)

s = 40 * "1" + 40 * "2"
while "111" in s:
    s = s.replace("111", "2", 1)
    s = s.replace("222", "1", 1)
print(s)


s = 85 * "9"
while "666" in s or "999" in s:
    if "666" in s:
        s = s.replace("666", "9", 1)
    else:
        s = s.replace("999", "6", 1)
print(s)


# Какая строка получится в результате применения приведённой ниже программы к строке длины 101, в которой первый и последний символ – это цифры 1, а остальные символы – цифры 8?

# В ответе запишите полученную строку.

s = "1" + "8" * 99 + "1"
while "81" in s or "882" in s or "8883" in s:
    if "81" in s:
        s = s.replace("81", "2", 1)
    elif "882" in s:
        s = s.replace("882", "3", 1)
    else:
        s = s.replace("8883", "1", 1)

print(s)