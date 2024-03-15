import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

if max(arr) == 0:
    print("SAD")
else:
    arr_sum = sum(arr[0:x])
    value = arr_sum
    count = 1

    for i in range(x, n):
        # 슬라이딩 윈도우
        value -= arr[i-x]
        value += arr[i]
        if value > arr_sum:
            arr_sum = value
            count = 1
        elif value == arr_sum:
            count += 1
    print(arr_sum)
    print(count)