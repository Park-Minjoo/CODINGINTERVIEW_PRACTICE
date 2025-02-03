def solution(n):
    return int((6 * n / gcd(6, n)) // 6)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a