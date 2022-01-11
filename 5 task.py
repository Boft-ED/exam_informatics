def alg(N):
    N = bin(N)[2:]

    if int(N, 2) % 2 == 0:
        N = "1" + N + "0"
    else:
        N = "11" + N + "00"

    return int(N, 2)


for N in range(1, 1000):
    if alg(N) > 52:
        print(N)
        break