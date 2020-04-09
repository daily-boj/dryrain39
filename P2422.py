F = lambda n: 1 if n <= 1 else n * F(n - 1)

if __name__ == '__main__':
    input_val = input().split(' ')
    no_ice_species, no_ex = int(input_val[0]), int(input_val[1])

    duplicate_list = []
    duplicate = 0

    for _ in range(no_ex):
        for element in input().split(' '):
            if int(element) in duplicate_list:
                duplicate += 1
            else:
                duplicate_list.append(int(element))

    print(int(F(no_ice_species) / (F(no_ice_species - 3) * F(3)) - ((no_ice_species - 2) * no_ex) + duplicate))
