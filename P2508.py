def is_candy(a, b, c, xy):
    return (a == '>' and b == 'o' and c == '<' and xy == 'x') or \
           (a == 'v' and b == 'o' and c == '^' and xy == 'y')


if __name__ == '__main__':
    test_count = int(input())

    for _ in range(test_count):
        input()
        height = int(input().split()[0])

        candy = 0

        tmp = [
            # line_number: [first_word, second_word, third_word]
            [] for x in range(401)
        ]

        for y in range(height):
            line = input()
            for x in range(len(line)):

                if line[x] == '>' and len(line) > x + 2:
                    if is_candy(line[x], line[x + 1], line[x + 2], 'x'):
                        candy += 1

                if line[x] == 'v':

                    tmp[x] = ['v']
                else:
                    tmp[x].append(line[x])

                if len(tmp[x]) == 3:
                    if is_candy(tmp[x][0], tmp[x][1], tmp[x][2], 'y'):
                        candy += 1

                    tmp[x] = []

        print(candy)
