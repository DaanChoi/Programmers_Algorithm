def solution1(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 " + str(i) + "에 있다"
print(solution1(["Jane", "Kim"]))

def solution2(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))
print(solution2(["Jane", "Kim"]))

# 아이디어
# 인덱스 찾는 방법1 => for반복문
# 인덱스 찾는 방법2 => list.index("element")
# 문자열 속 정수 표현 방법1 => "str" + str(int) + "str"
# 문자열 속 정수 표현 방법2 => "str {} str".format(int)
