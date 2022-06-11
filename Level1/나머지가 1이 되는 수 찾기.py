def solution(n):
    for i in range(2, n):
        if (n - 1) % i == 0:
            x = i
            break
    return x
print(solution(10))
print(solution(12)) 

# 아이디어
# n / x = 몫 ... 1
# n - 1 = x * 몫
# (n - 1)의 약수 중 1 제외하고 가장 작은 수가 x임
