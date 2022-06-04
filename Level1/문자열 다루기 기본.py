def solution1(s):
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False
print(solution1("a123"))
print(solution1("1234"))
print(solution1("12345"))

def solution2(s):
    return s.isdigit() and len(s) in {4, 6}
print(solution2("a123"))
print(solution2("1234"))
print(solution2("12345"))

def solution3(s):
    try:
        int(s)
    except:
        return False
    return len(s) in {4, 6}
print(solution3("a123"))
print(solution3("1234"))
print(solution3("12345"))

# 아이디어
# 정수로만 이뤄져 있는지 확인하는 방법1 => string.isdigit()
# 정수로만 이뤄져 있는지 확인하는 방법2 => 예외처리!!

# 예외처리

try:
    int("12345")
except: # 발생하는 에러의 종류 지정해줄 수도 있음(여기서는 종류에 에러 종류 상관없이 실행)
    print("error") # 에러가 있을 때 실행되는 코드
else:
    print("no error") # 에러가 없을 때 실행되는 코드
finally:
    print("end") # 에러 발생과 상관없이 항상 실행되는 코드

