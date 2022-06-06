def solution1(a, b):
    return sum(range(a, b + 1)) if a < b else sum(range(b, a + 1))
print(solution1(3, 5))
print(solution1(5, 3))
print(solution1(3, 3))

def solution2(a, b):
    return sum(range(min(a, b), max(a, b) + 1))
print(solution2(3, 5))
print(solution2(5, 3))
print(solution2(3, 3))

def solution3(a, b):
    return (a + b) * (abs(b - a) + 1) // 2
print(solution3(3, 5))
print(solution3(5, 3))
print(solution3(3, 3))

# 아이디어
# 두 정수 크기 비교 => if 또는 min(), max()
# 두 정수 사이 연속하는 수 => range()
# 합1 => sum
# 합2 => 가우스 정리
# 가우스 정리 사용
# S = 1+2+...+(n-1)+n
# S = n+(n-1)+...+2+1
# 2S = (n+1)+(n+1)+...+(n+1)+(n+1)
# 절댓값 함수 abs()
