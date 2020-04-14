if __name__ == '__main__':
    no_coin_species, target_value = list(map(int, input().split()))
    coin_list = []

    for _ in range(no_coin_species):
        current_coin = int(input())

        if target_value < current_coin:
            continue

        coin_list.append(current_coin)

    current_value = 0
    current_coin_count = 0

    while current_value < target_value:
        current_coin = coin_list.pop()
        nam_eun_gap = target_value - current_value

        ga_nung_get_su = nam_eun_gap // current_coin

        current_value += ga_nung_get_su * current_coin
        current_coin_count += ga_nung_get_su

    print(current_coin_count)

