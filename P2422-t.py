import copy

l = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 2, 10], [1, 2, 11], [1, 3, 4],
     [1, 3, 5], [1, 3, 6], [1, 3, 7], [1, 3, 8], [1, 3, 9], [1, 3, 10], [1, 3, 11], [1, 4, 5], [1, 4, 6], [1, 4, 7],
     [1, 4, 8], [1, 4, 9], [1, 4, 10], [1, 4, 11], [1, 5, 6], [1, 5, 7], [1, 5, 8], [1, 5, 9], [1, 5, 10], [1, 5, 11],
     [1, 6, 7], [1, 6, 8], [1, 6, 9], [1, 6, 10], [1, 6, 11], [1, 7, 8], [1, 7, 9], [1, 7, 10], [1, 7, 11], [1, 8, 9],
     [1, 8, 10], [1, 8, 11], [1, 9, 10], [1, 9, 11], [1, 10, 11], [2, 3, 4], [2, 3, 5], [2, 3, 6], [2, 3, 7], [2, 3, 8],
     [2, 3, 9], [2, 3, 10], [2, 3, 11], [2, 4, 5], [2, 4, 6], [2, 4, 7], [2, 4, 8], [2, 4, 9], [2, 4, 10], [2, 4, 11],
     [2, 5, 6], [2, 5, 7], [2, 5, 8], [2, 5, 9], [2, 5, 10], [2, 5, 11], [2, 6, 7], [2, 6, 8], [2, 6, 9], [2, 6, 10],
     [2, 6, 11], [2, 7, 8], [2, 7, 9], [2, 7, 10], [2, 7, 11], [2, 8, 9], [2, 8, 10], [2, 8, 11], [2, 9, 10],
     [2, 9, 11], [2, 10, 11], [3, 4, 5], [3, 4, 6], [3, 4, 7], [3, 4, 8], [3, 4, 9], [3, 4, 10], [3, 4, 11], [3, 5, 6],
     [3, 5, 7], [3, 5, 8], [3, 5, 9], [3, 5, 10], [3, 5, 11], [3, 6, 7], [3, 6, 8], [3, 6, 9], [3, 6, 10], [3, 6, 11],
     [3, 7, 8], [3, 7, 9], [3, 7, 10], [3, 7, 11], [3, 8, 9], [3, 8, 10], [3, 8, 11], [3, 9, 10], [3, 9, 11],
     [3, 10, 11], [4, 5, 6], [4, 5, 7], [4, 5, 8], [4, 5, 9], [4, 5, 10], [4, 5, 11], [4, 6, 7], [4, 6, 8], [4, 6, 9],
     [4, 6, 10], [4, 6, 11], [4, 7, 8], [4, 7, 9], [4, 7, 10], [4, 7, 11], [4, 8, 9], [4, 8, 10], [4, 8, 11],
     [4, 9, 10], [4, 9, 11], [4, 10, 11], [5, 6, 7], [5, 6, 8], [5, 6, 9], [5, 6, 10], [5, 6, 11], [5, 7, 8], [5, 7, 9],
     [5, 7, 10], [5, 7, 11], [5, 8, 9], [5, 8, 10], [5, 8, 11], [5, 9, 10], [5, 9, 11], [5, 10, 11], [6, 7, 8],
     [6, 7, 9], [6, 7, 10], [6, 7, 11], [6, 8, 9], [6, 8, 10], [6, 8, 11], [6, 9, 10], [6, 9, 11], [6, 10, 11],
     [7, 8, 9], [7, 8, 10], [7, 8, 11], [7, 9, 10], [7, 9, 11], [7, 10, 11], [8, 9, 10], [8, 9, 11], [8, 10, 11],
     [9, 10, 11]]

# 25가지 중에서 3가지 뽑은거
print(len(l))

ban_list = [
    [1, 2],
    [1, 3],
    [3, 4],
    [1, 4],
]

for ban_element in ban_list:
    for idx in range(len(copy.deepcopy(l))):
        if ban_element[0] in l[idx] and ban_element[1] in l[idx]:
            l[idx] = []

blank_cnt = 0
for element in l:
    if element == []:
        blank_cnt += 1

print(len(l))
print(blank_cnt)
print(len(l) - blank_cnt)
