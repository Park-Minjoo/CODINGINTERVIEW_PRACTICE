def solution(s):
    answer = ''
    arr = list(map(int, s.split()))
    minList = str(min(arr))
    maxList = str(max(arr))

    answer = minList + ' ' + maxList
    return answer