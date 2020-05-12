C = [5, 5]
C.extend([0 for x in range(9999999)])


def o_gak_hyeong(n):
    if C[n] != 0:
        return C[n]

    for idx in range(n):
        if C[idx] != 0:
            continue
        else:
            C[idx] = (C[idx - 1] + (idx + 1) + idx * 2) % 45678

    C[n] = (C[n - 1] + (n + 1) + n * 2) % 45678

    return C[n]


if __name__ == '__main__':
    print(o_gak_hyeong(int(input())))
