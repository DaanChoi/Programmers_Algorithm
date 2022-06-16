def solution0(n):
    ls = []
    while n != 1:
        ls.append(n % 3)
        n = n // 3
    ls.append(n)
    
    sum = 0
    for i in range(len(ls)):
        sum += ls[i] * pow(3, len(ls) - i - 1)
    
    return sum
print(solution0(45))
# 시간초과 됨..
# 시간초과 해결하기
# ref) https://velog.io/@suyeonpi/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-3%EC%A7%84%EB%B2%95-%EB%92%A4%EC%A7%91%EA%B8%B0-Python
def solution1(n):
    answer = ''
    
    while(n >= 1):
        rest = n % 3
        n = n // 3
        answer += str(rest)
    
    return int(answer, 3)
print(solution1(45))

def solution2(n):
    answer = ''

    while n >= 0:			
        n, re = divmod(n,3)	
        answer += str(re)
    return int(answer, 3)
print(solution2(45))

# 아이디어
# 3진법으로 바꾸기 => n을 3으로 계속 나누면서 나머지를 기록, 마지막에 몫 1까지 추가
# 이때 solution0에서는 리스트를 활용(append) 시간초과됨
# solution1에서는 문자열을 활용(문자열의 연산) 시간초과 안됨
# 리스트의 내장함수 append가 시간초과의 원인인건가? => 더 찾아봐야 함

# divmod(n, 3) => 몫과 나머지를 반환(튜플형식으로)
# int(x, 3) => 3진법으로 구성된 x를 10진법으로 바꿔줌
