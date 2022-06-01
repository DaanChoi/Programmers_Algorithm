def gcd(n, m):
    a = n if n > m else m
    b = m if n > m else n
    if b == 0:
        return a
    return gcd(m, n % m)
print(gcd(3, 12))

def solution1(n, m):
    g = gcd(n, m)
    l = g * (n // g) * (m // g)
    return [g, l]
print(solution1(3, 12))

import math

def solution2(n, m):
    return [math.gcd(n, m), math.lcm(n, m)]
print(solution1(3, 12))

def solution3(a, b):
    c, d = max(a, b), min(a, b)
    r = 1
    while r != 0:
        r = c % d
        c = d
        d = r
    return [c, (a * b) // c]
print(solution3(3, 12))

def solution4(n, m):
    gcd1 = lambda a, b: b if not a % b else gcd1(b, a % b)
    lcm1 = lambda a, b: (a * b) // gcd1(a, b)
    return [gcd1(n, m), lcm1(n, m)]
print(solution4(3, 12))

# 아이디어
# 최대공약수, 최소공배수 관련 문제는
# 유클리드 호제법을 생각해보자
# 유클리드 호제법을
# 3가지 방법으로 구현해 봄
