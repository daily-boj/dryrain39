if __name__ == '__main__':
    pikachu_str = input()

    while "pi" in pikachu_str or "ka" in pikachu_str or "chu" in pikachu_str:
        pikachu_str = pikachu_str.replace("pi", "_OK_")
        pikachu_str = pikachu_str.replace("ka", "_OK_")
        pikachu_str = pikachu_str.replace("chu", "_OK_")

    pikachu_str = pikachu_str.replace("_OK_", "")
    print("YES" if pikachu_str == "" else "NO")
