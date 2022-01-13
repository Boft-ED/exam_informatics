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