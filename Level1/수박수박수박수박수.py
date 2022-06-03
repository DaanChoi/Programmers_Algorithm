def solution1(n):
    if n % 2 == 0:
        return "수박" * (n // 2)
    else:
        return "수박" * (n // 2) + "수" * (n % 2)
print(solution1(3))
print(solution1(4))

def solution2(n):
    return "수박" * (n // 2) + "수" * (n % 2)
print(solution2(3))
print(solution2(4))

# 아이디어
# 나눈 몫만큼 반복
# 홀수라면 => 나머지 1인만큼 마지막에 "수" 한 번 추가
# 짝수라면 => 나머지가 0이므로 몫만큼 반복
