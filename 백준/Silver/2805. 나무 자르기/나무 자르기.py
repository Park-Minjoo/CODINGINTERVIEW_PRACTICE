n, m = map(int, input().split())
trees = list(map(int, input().split()))

end = max(trees)
start = 0

result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2

    for i in trees:
        if i > mid:
            count += i - mid
    if count >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)