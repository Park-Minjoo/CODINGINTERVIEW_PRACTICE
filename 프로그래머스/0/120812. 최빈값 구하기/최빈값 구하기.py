def solution(array):
    idx = [0] * 1001
    
    for i in array:
        idx[i] += 1
    if idx.count(max(idx)) > 1:
        return -1
    return idx.index(max(idx))