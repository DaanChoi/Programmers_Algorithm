def solution(dartResult):
    stack = []
    scoreDict = { 'S' : 1, 'D' : 2, 'T' : 3 }
    dartResult = dartResult.replace('10', 'A')
    for c in dartResult:
        if c.isdigit():
            stack.append(int(c))
        elif c == 'A':
            stack.append(10)
        
        elif c in {'S', 'D', 'T'}:
            num = stack.pop()
            stack.append(num ** scoreDict[c])
        
        elif c == '*':
            if len(stack) > 1:
                stack[-1] *= 2
                stack[-2] *= 2
            else:
                stack[-1] *= 2
        elif c == '#':
            stack[-1] *= -1
    return sum(stack)
print(solution("1S2D*3T"))
print(solution("1D2S#10S"))

# 아이디어
# 문자열 또는 리스트에서 구간별로 연산 처리가 많다면 => 스택 고려
# 문자열에서 예외 문자 처리 => replace 고려
# 문자별로 수가 할당되어 있다 => 딕션너리
