# Для игры, описанной в предыдущем задании, найдите два таких значения S,
# при которых у Пети есть выигрышная стратегия, причём одновременно выполняются
# два условия:
# -Петя не может выиграть за один ход;
# - Петя может выиграть своим вторым ходом независимо от того, как будет ходить
# Ваня.
# Найденные значения запишите в ответе в порядке возрастания.
def f(x, y, p):
    if x + y >= 142 and p == 4:
        return True
    else:
        if x + y < 142 and p == 4:
            return False
        else:
            if x + y >= 142:
                return False
    if p % 2 == 1:
        return f(x + 2, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 2, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 2, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 2, p + 1) and f(x, y * 2, p + 1)
for i in range(1, 100 +1):
    if f(2, i, 1):
        print(i)

# ответ 67 68

# Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:

# — Петя не может выиграть за один ход;

# — Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

# Найденные значения запишите в ответе в порядке возрастания без разделительных знаков.

def f(x, p):
    if x >= 81 and p == 4:
        return True
    else:
        if x < 81 and p == 4:
            return False
        else:
            if x >= 81:
                return False
    if p % 2 == 1:
        return f(x + 1, p + 1) or f(x * 4, p + 1)
    else:
        return f(x + 1, p + 1) and f(x * 4, p + 1)
for s in range(1, 100 +1):
    if f(s, 1):
        print(s)

#Задание 20 № 27766 Добавить в вариант

def f(x, y, p):
    if x + y >= 69 and p == 4:
        return True
    else:
        if x + y < 69 and p == 4:
            return False
        else:
            if x + y >= 69:
                return False
    if p % 2 == 1:
        return f(x+1, y, p+1) or f(x, y+1, p+1) or f(x*2, y, p+1) or f(x, y*3, p+1)
    else:
        return f(x+1, y, p+1) and f(x, y+1, p+1) and f(x*2, y, p+1) and f(x, y*3, p+1)
for s in range(1, 58 +1):
    if f(10, s, 1):
        print(s)








def f(x,y,p):
    if x + y >= 151 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x + 1,y, p + 1) or f(x,y + 1, p + 1) or f(x * 4, y , p + 1) or f(x, y * 4, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 4, y, p + 1) and f(x, y * 4, p + 1)


for s in range(1, 141):
    if f(9,s,0):
        print(s)


