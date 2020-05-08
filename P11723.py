from sys import stdin

infast = lambda: stdin.readline().strip()
Q = {
    "add": lambda s, q: s.add(q),
    "remove": lambda s, q: s.remove(q) if q in s else 0,
    "check": lambda s, q: print(1 if q in s else 0),
    "toggle": lambda s, q: s.remove(q) if q in s else s.add(q),
    "all": lambda s, q: (s.clear(), s.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])),
    "empty": lambda s, q: s.clear(),
}

if __name__ == '__main__':
    s = set()

    for _ in range(int(input())):
        query = infast().split()

        Q[query[0]](s, 0) if len(query) < 2 else Q[query[0]](s, int(query[1]))
