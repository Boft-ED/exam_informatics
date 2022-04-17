# Для игры, описанной в задании 19, найдите минимальное значение S, при котором
# одновременно выполняются два условия:
# - у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым
# ходом при любой игре Пети;
# - у Вани нет стратегии, которая позволит ему гарантированно выиграть первым
# ходом.

def f(x, y, p):
    if x + y >= 142 and (p == 5 or p == 3):
        return True
    else:
        if x + y < 142 and p == 5:
            return False
        else:
            if x + y >= 142:
                return False
    if p % 2 == 0:
        return f(x + 2, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 2, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 2, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 2, p + 1) and f(x, y * 2, p + 1)

def f1(x, y, p):
    if x + y >= 142 and p == 3:
        return True
    else:
        if x + y < 142 and p == 3:
            return False
        else:
            if x + y >= 142:
                return False
    if p % 2 == 0:
        return f1(x + 2, y, p + 1) or f1(x * 2, y, p + 1) or f1(x, y + 2, p + 1) or f1(x, y * 2, p + 1)
    else:
        return f1(x + 2, y, p + 1) and f1(x * 2, y, p + 1) and f1(x, y + 2, p + 1) and f1(x, y * 2, p + 1)

for i in range(1, 100 +1):
    if f(2, i, 1):
        print(i)
print("=====")
for i in range(1, 100 +1):
    if f1(2, i, 1):
        print(i)

# ответ 66

# Найдите минимальное значение S, при котором одновременно выполняются два условия:

# — у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;

# — у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

def f(x, p):
    if x >= 81 and (p == 5 or p == 3):
        return True
    else:
        if x < 81 and p == 5:
            return False
        else:
            if x >= 81:
                return False
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x * 4, p + 1)
    else:
        return f(x + 1, p + 1) and f(x * 4, p + 1)

def f1(x, p):
    if x >= 81 and p == 3:
        return True
    else:
        if x < 81 and p == 3:
            return False
        else:
            if x >= 81:
                return False
    if p % 2 == 0:
        return f1(x + 1, p + 1) or f1(x * 4, p + 1)
    else:
        return f1(x + 1, p + 1) and f1(x * 4, p + 1)

for s in range(1, 100 +1):
    if f(s, 1):
        print(s)
print("=====")
for s in range(1, 100 +1):
    if f1(s, 1):
        print(s)


def f(x, p):
    if x >= 22 or p > 5:
        return p == 3 or p == 5
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 2, p + 1) and f(x * 2, p + 1)

for s in range(1, 21 + 1):
    if f(s, 1):
        print(s)
