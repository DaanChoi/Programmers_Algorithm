def solution1(n):
    cnt = 0
    while n != 1 and cnt != 500:
        if n % 2 == 0:
            n /= 2
            cnt += 1
        else:
            n = 3 * n + 1
            cnt += 1
    return cnt if cnt != 500 else -1
print(solution1(626331))
print(solution1(1))

def solution2(n):
    for i in range(500):
        if n == 1:
            return i
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return -1
print(solution1(626331))
print(solution1(1))

# 아이디어
# 반복문 종료조건에 break가 아닌 return을 써서 코드 간단히 함
# 반복문에는 while문과 for문이 있으니 적절하게 선택해서 사용하기 
