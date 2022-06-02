def solution1(x):
    sum = 0
    for c in str(x):
        sum += int(c)
    
    if x % sum == 0:
        return True
    else:
        return False
print(solution1(18))

def solution2(x):
    return x % sum([int(c) for c in str(x)]) == 0
print(solution2(18))

# 아이디어
# solution1에서
# 자연수의 각 자릿수 합을 구하기 위해서 우선 문자열 자료형으로 바꾸는 것을 생각함
# 그리고 각 문자열의 문자들을 정수형으로 바꿔서 합함
# solution2에서
# 코드를 더 간단히 하기 위해서
# 리스트 컨프리헨션 사용 / sum 내장함수 사용 / 관계연산자는 boolean 반환하는 성질 사용
