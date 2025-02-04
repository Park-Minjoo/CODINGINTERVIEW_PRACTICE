def longestConsecutive(nums):
    longest = 0
    numsDic = {}
    for num in nums:
        numsDic[num] = True

    for num in nums:
        if num - 1 not in numsDic: # 나보다 1 작은 수가 없으면 가장 작은 수
            cnt = 0
            target = num + 1
            while target in numsDic:
                cnt += 1
                target += 1
            longest = max(cnt, longest)
    return longest

longestConsecutive([6, 7, 100, 5, 4, 4, 8])