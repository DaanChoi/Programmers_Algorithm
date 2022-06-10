def solution(n, arr1, arr2):
    e = [2 ** i for i in range(n - 1, -1, -1)]
    b1 = ['' for i in range(n)]
    b2 = ['' for i in range(n)]
    result = ['' for i in range(n)]

    for i in range(n):
        for j in range(n):
            if arr1[i] >= e[j]:
                b1[i] += '1'
                arr1[i] -=e[j]
            elif arr1[i] < e[j]:
                b1[i] += '0'
    
    for i in range(n):
        for j in range(n):
            if arr2[i] >= e[j]:
                b2[i] += '1'
                arr2[i] -=e[j]
            elif arr2[i] < e[j]:
                b2[i] += '0'

    for i in range(n):
        for j in range(n):
            if int(b1[i][j]) or int(b2[i][j]):
                result[i] += '#'
            else:
                result[i] += ' '
    
    return result
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# 아이디어
# 10진수를 2진수로 바꿈 => 2의 n제곱을 순차적으로 빼기
# 비트 연산으로 해독한 지도 만들기 => or 연산
# for문 거꾸로 반복하기 => step을 음수로 => range(n, 0, -1)
# if if <=> if elif 조심하기
