def solution1(n):
    sum = 0 
    for x in range(1, n + 1):
        if n % x == 0:
            sum += x
    return sum
print(solution1(12))
print(solution1(5))

def solution2(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])
print(solution2(12))
print(solution2(5))

def solution3(n):
    sum = 0
    for x in range(1, n // 2 + 1):
        if n % x == 0:
            sum += x
    sum += n
    return sum
print(solution3(12))
print(solution3(5))

# 아이디어
# 약수 찾기 => 약수는 해당 자연수를 나눴을 때 나머지가 0인 거
# 최적화 => 자연수 본인 외에는 모든 약수는 자연수의 1/2이하임
