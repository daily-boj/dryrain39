def layer_append(layer_list, x):
    for n in range(x):
        layer_list[n] += 1


if __name__ == '__main__':
    layer_info = [0 for _ in range(10000001)]
    N = int(input())

    input_sum = 0
    input_cnt = N * N
    # input_max_layer = 0

    for y in range(N):
        x_list = list(map(int, input().split()))

        for x in x_list:
            input_sum += x
            layer_append(layer_info, x)

    if input_sum == 0:
        print(0)
        exit()

    target = input_sum / 2
    layer_sum = 0
    for idx in range(10000001):
        layer_sum += layer_info[idx]
        if layer_sum >= target:
            print(idx + 1)
            break
