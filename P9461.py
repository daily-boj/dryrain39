initial = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]


def request(n):
    while len(initial) < n + 1:
        initial.append(initial[-3] + initial[-2])

    return initial[n]


if __name__ == '__main__':
    for _ in range(int(input())):
        print(request(int(input())))
