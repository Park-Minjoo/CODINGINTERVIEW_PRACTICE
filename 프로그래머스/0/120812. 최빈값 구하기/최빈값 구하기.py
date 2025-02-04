# def solution(array):
#     cnt = [0] * 1001
#     for arr in array: # 1
#         for i in range(len(array)):
#             print(i)
#             if arr == array[i]: # arr = 1 2 arr[0] = 1
#                 cnt[arr] += 1 # cnt[0] = 1
#     print(cnt)
#     answer = 0
#     return answer

# Solution 1
def solution(array):
    answer = 0
    idx = [0] * 1001
    for i in array:
        idx[i] += 1
    if idx.count(max(idx)) > 1:
        return -1
    return idx.index(max(idx))
    # print(idx)
array = [1, 2, 3, 3, 3, 4]
print(solution(array))

#Solution2
def solution2(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1