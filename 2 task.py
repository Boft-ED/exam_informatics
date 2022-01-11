print("a b c d")

for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                F = (a <= b) and (not(b == c)) and (d <= a)
                if bool(F):
                    print(a, b, c, d)