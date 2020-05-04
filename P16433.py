def jjak(x):
    return x % 2 == 0


if __name__ == '__main__':
    N, R, C = list(map(int, input().split()))

    mod = True

    if (jjak(R) and not jjak(C)) or (not jjak(R) and jjak(C)):
        mod = False

    for a in range(N):
        for b in range(N):
            print("v" if jjak(b) == mod else ".", end='')
        print("\n", end='')
        mod = not mod
