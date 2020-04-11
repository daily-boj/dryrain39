def select_min(p1, p2):
    return p1 if p1 < p2 else p2


if __name__ == '__main__':
    pizza = {
        "1/4": 0,
        "1/2": 0,
        "3/4": 0,
        "full": 0
    }

    for _ in range(int(input())):
        pizza_type = input().strip()
        pizza[pizza_type] += 1

    # 1/4 + 3/4
    if pizza["1/4"] and pizza["3/4"]:
        min_cnt = select_min(pizza["1/4"], pizza["3/4"])
        pizza["1/4"] -= min_cnt
        pizza["3/4"] -= min_cnt

        pizza["full"] += min_cnt

    # 1/2 * 2
    if pizza["1/2"] >= 2:
        min_cnt = pizza["1/2"] // 2
        pizza["1/2"] -= min_cnt * 2

        pizza["full"] += min_cnt

    # 1/2 + 1/4 * 2
    if pizza["1/2"] and pizza["1/4"] // 2:
        min_cnt = select_min(pizza["1/2"], pizza["1/4"] // 2)
        pizza["1/2"] -= min_cnt * 1
        pizza["1/4"] -= min_cnt * 2

        pizza["full"] += min_cnt

    # 1/4 * 4
    if pizza["1/4"] // 4:
        min_cnt = pizza["1/4"] // 4
        pizza["1/4"] -= min_cnt * 4

        pizza["full"] += min_cnt

    print(pizza["1/2"] + pizza["1/4"] + pizza["3/4"] + pizza["full"])
