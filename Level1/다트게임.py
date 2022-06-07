def solution(dartResult):
  dartResult = dartResult.replace('10', 'A')
  stack = []
  scores = { 'S' : 1, 'D' : 2, 'T' : 3 }
  
  for c in dartResult:
    if c.isnumeric():
      stack.append(int(c))
    elif c == "A":
      stack.append(10)
      
    elif c in {'S', 'D', 'T'}:
      num = stack.pop()
      stack.append(num ** scores[c])
      
    elif c == '*':
      if len(stack) > 1:
        stack[-1] *= 2
        stack[-2] *= 2
      else:
        stack[-1] *= 2
    elif c == '#':
      stack[-1] *= (-1)

  return sum(stack)
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S2D*3T"))
print(solution("1S*2T*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))

# 아이디어
# 문자열에서 예외처리('10') => str.replace()
# 특정 문자가 특정 정수값을 갖는다 => dictionary 자료형
# 리스트에서 수정 잦다 => stack 개념(append, pop, [-1])
# -index => stack의 pop과 같은 인덱싱 / 원소접근과 계산이 연속적일 때 고려해볼만함

# 참고 https://velog.io/@highero-k/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A4%ED%8A%B8-%EA%B2%8C%EC%9E%84-Python-Level-1

# 틀린 코드..
# def solution(dartResult):

#     index = 0
#     arr = [[] for _ in range(5)] # 이중리스트 초기화는 리스트 컴프리헨션으로
#     scores = {
#         "S" : 1,
#         "D" : 2,
#         "T" : 3
#     } # 문자 별로 점수(정수) 할당

#     # 각 기회별로 문자열 나눠담기(arr 리스트에)
#     for c in dartResult:
#         if c.isdigit():
#             index += 1
#         arr[index].append(c)
#     # 문자열에 10이 있을 때 예외 처리하는 코드
#     rm_index = -1
#     for i in range(len(arr)):
#         if arr[i] == ['1']:
#             rm_index = i
#             arr[i] += arr[i + 1]
#             arr[i][0] += arr[i][1]
#     if rm_index > 0:
#         arr.remove(arr[rm_index + 1])
#         arr[rm_index].remove(arr[rm_index][1])

#     # 점수 측정하기(일단 "*" 중복은 고려하지 않고), 점수를 result 리스트에 담기
#     result = [0]
#     for i in range(1, 4):
#         if len(arr[i]) == 3:
#             if arr[i][2] == "*":
#                 result.append(pow(int(arr[i][0]), scores[arr[i][1]]) * 2)
#             if arr[i][2] == "#":
#                 result.append(pow(int(arr[i][0]), scores[arr[i][1]]) * (-1))
#         else:
#             result.append(pow(int(arr[i][0]), scores[arr[i][1]]))

#     # "*" 중복 고려해서 해당 부분만 점수 다시 측정
#     for i in [2, 3]:
#         if len(arr[i]) == 3 and arr[i][2] == "*":
#             result[i - 1] *= 2

#     return sum(result)
# print(solution("1D2S#10S"))
# print(solution("1D2S0T"))
# print(solution("1S2D*3T"))
# print(solution("1S*2T*3S"))
# print(solution("1T2D3D#"))
# print(solution("1D2S3T*"))
