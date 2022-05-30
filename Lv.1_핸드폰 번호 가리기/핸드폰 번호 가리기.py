def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]
print(solution("01033334444"))
print(solution("027778888"))

#아이디어
#문자열은 인덱싱, 슬라이싱 가능하나
#어싸인먼트(원소 교체)가 안됨. 따라서 문자열 연산을 사용
