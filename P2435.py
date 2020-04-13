if __name__ == '__main__':
    M = int(input().split()[1])
    value_list = list(map(int, input().split()))
    sum_max = None

    for n in range(len(value_list) - M + 1):
        current = sum(value_list[n:n + M])
        if sum_max is None or current > sum_max:
            sum_max = current

    print(sum_max)
