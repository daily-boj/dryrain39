def kap_to_arr(number: int) -> list:
    return ([0, 0, 0, 0] + list(map(int, str(number))))[-4:]


def kap_to_int(arr: list, reverse: bool = False) -> int:
    return int("".join(sorted(map(str, arr), reverse=reverse)))


def kaprekar(inp: str) -> int:
    numbers = list(map(int, inp))
    result = int(inp)
    loop_count = 0

    while result != 6174:
        _min = kap_to_int(numbers)
        _max = kap_to_int(numbers, reverse=True)

        loop_count += 1
        result = _max - _min

        numbers = kap_to_arr(result)

    return loop_count


if __name__ == '__main__':
    for ___ in range(int(input())):
        print(kaprekar(input()))
