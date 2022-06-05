def solution1(s):
    p_cnt = 0
    y_cnt = 0
    s = s.lower()

    for c in s:
        if c == 'p':
            p_cnt += 1
        if c == 'y':
            y_cnt += 1
    
    return  p_cnt == y_cnt

print(solution1("pPoooyY"))
print(solution1("Pyy"))

def solution2(s):
    return s.lower().count('p') == s.lower().count('y')

print(solution2("pPoooyY"))
print(solution2("Pyy"))

def solution3(s):
    p_cnt = 0
    y_cnt = 0

    for c in s:
        if c in {'p', 'P'}:
            p_cnt += 1
        if c in {'y', 'Y'}:
            y_cnt += 1
    
    return p_cnt == y_cnt

print(solution3("pPoooyY"))
print(solution3("Pyy"))

# 아이디어
# 1
# 소문자, 대문자 구별하지 않음 
# => 문자열 모두 소문자로 만듦(또는 모두 대문자로) 
# => str.lower() : 대문자를 소문자로
# => str.upper() : 소문자를 대문자로
# 'p', 'y'의 개수를 셈 => for문 / if문 비교연산자 또는 in {}
# 비교연산자 if문 사용하고 리턴할 때 => 그냥 return 비교연산자로 한줄 작성하면 됨

# 2
# count() 함수는 리스트 뿐만 아니라 문자열에도 사용 가능

# 3
# 굳이 모두 소문자로 만들지 않아도 'p', 'P', 'y', 'Y' 개수 세면 됨
# => 비교연산자 또는 in {}