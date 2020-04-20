from sys import stdin

qwerty = {' ': 0, '`': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 10, '-': 11,
          '=': 12, 'Q': 13, 'W': 14, 'E': 15, 'R': 16, 'T': 17, 'Y': 18, 'U': 19, 'I': 20, 'O': 21, 'P': 22, '[': 23,
          ']': 24, '\\': 25, 'A': 26, 'S': 27, 'D': 28, 'F': 29, 'G': 30, 'H': 31, 'J': 32, 'K': 33, 'L': 34, ';': 35,
          "'": 36, 'Z': 37, 'X': 38, 'C': 39, 'V': 40, 'B': 41, 'N': 42, 'M': 43, ',': 44, '.': 45, '/': 46}


def generator():
    q = {' ': 0}
    s = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
    for i in range(len(s)):
        q[s[i]] = i
    print(q)


if __name__ == '__main__':
    qwerty_keys = list(qwerty.keys())

    for line in stdin:
        answer = ""
        for char in line:
            if char == '\n':
                continue
            answer += qwerty_keys[qwerty[char]]

        print(answer)
