if __name__ == '__main__':
    row, col = list(map(int, input().split()))

    x1, y1, x2, y2 = None, None, None, None

    for current_row in range(row):
        cr_input = input().replace(" ", "")

        for current_col in range(len(cr_input)):
            if cr_input[current_col] == "1":
                if x1 is None:
                    x1 = current_col
                    y1 = row - current_row - 1
                else:
                    x2 = current_col
                    y2 = row - current_row - 1

    print(abs(x2 - x1) + abs(y2 - y1))
