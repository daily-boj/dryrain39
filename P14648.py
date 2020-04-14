def q1(a, q):
    # q0번째부터 q1번째까지 합
    result = sum(a[q[0] - 1:q[1]])
    # q0과 q1을 스왑
    a[q[0] - 1], a[q[1] - 1] = a[q[1] - 1], a[q[0] - 1]

    return result


def q2(a, q):
    # (q0 + q1) - (q2 - q3)
    return sum(a[q[0] - 1:q[1]]) - sum(a[q[2] - 1:q[3]])


if __name__ == '__main__':
    _, no_query = list(map(int, input().split()))
    su_yeol = list(map(int, input().split()))

    query_list = [None, q1, q2]

    for _ in range(no_query):
        query = list(map(int, input().split()))
        query_result = query_list[query[0]](su_yeol, query[1:])
        print(query_result)
