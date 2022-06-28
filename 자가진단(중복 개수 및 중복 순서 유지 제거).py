# arr = [1,2,3,3,3,3,4,4]
# arr = [3,5,7,9,1]
arr = [3,2,4,4,2,5,2,5,5]
arr_set = set(arr)
dict = {}
answer = []
check = []

for i in arr_set:
    dict[i] = 0

for a in arr:
    if a in arr_set:
        dict[a] += 1

print(dict)

for a in arr:
    if a not in check and dict[a] > 1:
        check.append(a)
        answer.append(dict[a])
if len(answer) == 0:
    answer = [-1]

print(answer)

# 중복 제거하되 순서 유지하기
# 반복문을 돌면서 각 원소들 탐색
# 별도의 check 리스트를 만들어서 
# check 리스트에 없다면 추가.
