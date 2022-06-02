def solution1(arr):
    arr.remove(min(arr))
    return arr if len(arr) != 0 else [-1]
print(solution1([4,3,2,1]))

def solution2(arr):
    answer = [i for i in arr if i > min(arr)]
    return answer if len(answer) != 0 else [-1]
print(solution2([4,3,2,1]))

def solution3(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]
print(solution3([4,3,2,1]))

# 아이디어
# 리스트에서 가장 작은 원소 찾기 => min
# 가장 작은 원소 제거하기 => remove or 리스트 컴프리헨션
