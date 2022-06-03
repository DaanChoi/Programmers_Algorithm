print(ord('a'))
print(ord('A'))
print(ord('z'))
print(ord('Z'))

def solution(s, n):
    answer = ''
    for c in s:
        if c.islower():
            answer += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        elif c.isupper():
            answer += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += c
    return answer
print(solution("a B z", 4))

# 아이디어
# 문자에 정수를 더하고 결과를 문자로 => 아스키 코드
# 아스키 코드 변환 함수 => ord(), chr()
# 'z'를 넘어가면 다시 'a'로 돌아감 => 식을 세움
# 대문자인 경우 소문자인 경우, 특수문자인 경우, 특수문자인 경우 => if 조건문
