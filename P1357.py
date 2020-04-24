Rev = lambda z: int(''.join(list(reversed([_ for _ in str(z)]))))

if __name__ == '__main__':
    x, y = list(input().split())
    print(Rev(Rev(x) + Rev(y)))
