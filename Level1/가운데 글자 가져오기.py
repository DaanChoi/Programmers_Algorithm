def solution(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]
    if len(s) % 2 == 1:
        return s[len(s) // 2]
print(solution("abcde"))
print(solution("qwer"))

def solution1(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]
print(solution1("abcde"))
print(solution1("qwer"))

# 아이디어
# 짝수인 경우, 홀수인 경우 나눠서 return
# 경우를 나누지 않아도 하나의 식으로 두 가지 경우를 다 처리 할 수도 있음
