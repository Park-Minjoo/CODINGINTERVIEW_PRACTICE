def solution(array):
    array = sorted(array)
    return array[len(array)//2]

print(solution([9, -1, 0]))