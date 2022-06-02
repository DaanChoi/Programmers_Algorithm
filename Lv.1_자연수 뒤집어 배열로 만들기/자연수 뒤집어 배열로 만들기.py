def solution(n):
    return list(map(int, reversed(str(n))))
print(solution(12345))

# 아이디어
# 뒤집기 => reversed()사용 : list뿐만 아니라 str 자료형도 사용 가능(reverse는 list만 사용 가능), 뒤집어진 객체를 반환하기 때문에 자료형을 설정해서 표현해야 함.
# 리스트의 각 원소들 자료형 정수형으로 변환하기 => map() 사용
