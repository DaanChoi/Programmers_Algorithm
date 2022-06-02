def solution1(n):
    x = n ** 0.5
    if x == int(x):
        return pow(x + 1, 2) #(x + 1) ** 2
    else:
        return -1
print(solution1(121))

def solution2(n):
    x = n ** 0.5
    if x % 1 == 0:
        return pow(x + 1, 2) #(x + 1) ** 2
    else:
        return -1
print(solution1(121))

import math

def solution3(n):
    x = math.sqrt(n)
    if x % 1 == 0:
        return pow(x + 1, 2) #(x + 1) ** 2
    else:
        return -1
print(solution3(121))

# 아이디어
# 제곱근 구하기 => x ** 0.5  또는 math 패키지의 math.sqrt()
# 정수인지 소수인지 판별하기 => x == int(x) 또는 x % 1 == 0
