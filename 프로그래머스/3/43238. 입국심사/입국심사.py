def solution(n, times):
    left, right = 1, max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total_people = sum(mid // time for time in times)

        if total_people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer