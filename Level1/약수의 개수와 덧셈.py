def solution(left, right):
    sum = 0
    for x in range(left, right + 1):
        cnt = 1
        for i in range(1, x // 2 + 1):
            if x % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            sum += x
        else:
            sum -= x
    return sum
print(solution(13, 17))

# 아이디어
# 약수의 개수 세기 => 나눴을 때 0이 되는 것 세기(조건문 사용)
# 나눴을 때 0이 되는 원소 찾기 => 범위의 반만큼만 반복문 사용해도 됨, 대신 본인자신 1을 더해줘야 함
