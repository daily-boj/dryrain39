# 문제 1935: 후위 표기식 2

CAL = {
    '+': lambda x, y: y + x,
    '-': lambda x, y: y - x,
    '*': lambda x, y: y * x,
    '/': lambda x, y: y / x,
}

if __name__ == '__main__':
    no_operand = int(input())  # 피연산자 갯수
    expression = [x for x in input()]  # 표기식
    expression_value = []

    # 피연산자 갯수만큼 입력
    for op_idx in range(no_operand):
        expression_value.append(int(input()))

    # 연산
    calculate_stack = []
    for element in expression:
        if element in CAL.keys():
            # 두 개 pop 해서 연산
            calculate_stack.append(CAL[element](calculate_stack.pop(), calculate_stack.pop()))
        else:
            calculate_stack.append(expression_value[ord(element) - 65])

    # 결과 출력
    print('%.2f' % calculate_stack[0])
