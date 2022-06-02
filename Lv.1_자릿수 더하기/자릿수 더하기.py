def solution1(n):
    return sum(list(map(int, list(str(n)))))
print(solution1(123))
print(solution1(987))

def solution2(n):
    if n < 10:
        return n
    return (n % 10) + solution2(n // 10)
print(solution2(123))
print(solution2(987))

# 아이디어
# 각 자릿수 더하기 1st => sum() 사용하기 위해서 각 자릿수를 원소로 갖는 리스트 만듦
# 각 자릿수 => 10으로 나눴을 때 나머지
# 각 자릿수 더하기 2nd => 재귀함수 사용(종료조건과 인자 설정 중요)
