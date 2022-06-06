def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x: x[n])
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))

# 아이디어
# 해당 인덱스의 문자가 같을 경우 사전 순으로 정렬 => 처음에 사전 순으로 한번 정렬해줌 그 다음에 인덱스 기준 정렬
# 해당 인덱스를 기준으로 정렬 => sorted() 함수 내에  key 속성 사용
# key 속성 사용 => 람다로 기준 설정
# 람다 인자(x)로 ["sun", "bed", "car"] 리스트 원소를 받고 원소의 1번째 인덱스 원소를 반환
