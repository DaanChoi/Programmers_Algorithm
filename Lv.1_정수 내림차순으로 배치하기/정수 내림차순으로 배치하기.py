def solution(n):
    ls = sorted(list(str(n)), reverse = True)
    return int(''.join(ls))
print(solution(118372))

# 아이디어
# 정수의 각 자릿수를 정렬
# 정수 -> 문자열 -> 리스트 -> 내림차순 정렬 -> 문자열 -> 정수
