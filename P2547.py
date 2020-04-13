if __name__ == '__main__':
    loop_count = int(input())

    for _ in range(loop_count):
        input()
        student_count = int(input())
        candy = 0

        for __ in range(student_count):
            usr_input = input()

            candy += int(usr_input)

        print("YES" if candy % student_count == 0 else "NO")
