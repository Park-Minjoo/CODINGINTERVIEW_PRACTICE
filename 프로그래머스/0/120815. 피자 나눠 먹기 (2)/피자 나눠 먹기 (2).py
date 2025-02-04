def solution(n):
    return int((6 * n / gcd(6, n)) // 6)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    for i in range(max(a, b), (a*b)+1):
        if i % a==0 and i % b == 0:
            return i



def lcm2(a, b):
    return a*b/gcd(a, b)
# 최소 공배수 6 and n
print(solution(6))
print(solution(10))
print(solution(4))
'''
# 1. 처음에 한 생각, 최소 공배수인가?
# 2. 아님 .. ㅌㅌㅋㅋㅋㅋㅋ ㅠㅠ

# case 1. 6의 배수: 6 12 18 24
# case 2.
# 1명이면 -> 1판
# 2명이면 -> 6조각을 3조각씩 -> 1판
# 3명이면 -> 6조각을 2조각씩 -> 2판 => 최대공약수가 6이면 1판
# 4명이면 -> 6 4 최소공배수 ? 최대공약수 ? 2? 아 .. 잠깐만
# 최소 공배수가 맞았네 
# 6조각이니까 한 판으로 만들어야지
# 다시 위로 올라갑니다
def solution(n):
    if n % 6 == 0: # 6의 배수
        return n // 6
    elif
'''