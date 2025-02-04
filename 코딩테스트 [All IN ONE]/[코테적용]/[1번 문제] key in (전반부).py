def TwoSum(nums, target):
    dictNum = {}
    for i, v in enumerate(nums):
        dictNum[v] = i
    print(dictNum)

    for v in nums:
        n = target - v
        if n in dictNum:
            if n == v: return False
            return dictNum[n], dictNum[v]
    return False

TwoSum([2, 1, 5, 7], 4)