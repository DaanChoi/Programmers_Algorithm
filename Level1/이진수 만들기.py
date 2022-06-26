n = 5
arr1 = [9, 20, 28, 18, 11]
result1 = ['' for i in range(n)]
for i in range(n):
    while arr1[i] >= 1:
        result1[i] += str(arr1[i] % 2)
        arr1[i] //= 2
    if len(result1[i]) != 5:
        result1[i] += '0'
    result1[i] = ''.join(reversed(result1[i]))

print(result1)

# 번외 : 이진수 만들기
# 2로 계속 나누며서 2로 나눈 나머지를 문자열로 만듦
# 만들어진 문자열은 이진수의 뒷자리부터 연산됐기 땜에 각 문자열을 뒤집는 과정 필요
# 문자열 뒤집기 => 2가지 방법
# 1. list로 변환하고 list.reverse() 사용, 그리고 다시 문자열로 join
# 2. reversed()와 join 사용
