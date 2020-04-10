def F(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


if __name__ == '__main__':
    input_val = input().split(' ')
    no_ice_species, no_ex = int(input_val[0]), int(input_val[1])

    duplicate_list = []
    duplicate_cnt = 0

    for _ in range(no_ex):
        except_input = input().split(' ')
        a, b = int(except_input[0]), int(except_input[1])

        for i in range(1, no_ice_species + 1):
            if a == i or b == i or a > no_ice_species or b > no_ice_species:
                continue

            x, y, z = a, b, i

            if x > y:
                x, y = y, x
            if y > z:
                y, z = z, y
            if x > y:
                x, y = y, x

            dup_element = (x * 1000000) + (y * 1000) + z

            if dup_element in duplicate_list:
                continue
            else:
                duplicate_list.append(dup_element)
                duplicate_cnt += 1

    print(int(no_ice_species * (no_ice_species - 1) * (no_ice_species - 2) / 6 - duplicate_cnt))
