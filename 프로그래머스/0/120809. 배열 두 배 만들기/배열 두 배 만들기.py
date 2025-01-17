def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]*2
    return numbers

print(solution([1,2,3,4,5]))