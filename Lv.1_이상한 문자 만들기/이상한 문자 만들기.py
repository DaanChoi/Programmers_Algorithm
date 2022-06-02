def solution(s):
    answer = ''
    ls = s.split()
    for c in ls:
        for i in range(len(c)):
            if i % 2 == 0:
                answer += c[i].upper()
            else:
                answer += c[i].lower()
        answer += ' '
    return answer[0:-1]
print(solution("try hello world"))

# 아이디어
# 문자열을 공백 기준으로 나눠서 리스트로 반환 => str.split()
# 짝수 인덱스일 때 원소 대문자로 바꾸기 => str.upper() 사용 그리고 문자열이기 때문에 원소 갱신할 때 어싸인먼트가 아니라 문자열 연산을 사용
# 홀수 인덱스일 때 원소 소문자로 바꾸기 => str.lower() 사용 그리고 이하 동문
