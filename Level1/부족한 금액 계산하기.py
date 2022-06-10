def solution(price, money, count):
    sum = 0
    for i in range(1, count + 1):
        sum += price * i
    return sum - money if sum > money else 0
print(solution(3, 20, 4))

# 아이디어
# 단순하게 로직 논리를 따라가면서 코딩
