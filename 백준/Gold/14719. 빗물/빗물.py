import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, w-1): # arr[i]에 담긴 물
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])
    # print(arr[:i], arr[i+1:])

    compare = min(left_max, right_max)
    # print('min: ', compare)
    if arr[i] < compare:
        ans += compare - arr[i]
        # print(compare - arr[i])
print(ans)