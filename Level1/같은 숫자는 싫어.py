def solution1(arr):
    ls = []
    for x in arr:
        if ls[-1:] == [x]:
            continue
        ls.append(x)
    return ls
print(solution1([1,1,3,3,0,1,1]))
print(solution1([4,4,4,3,3]))

def solution2(arr):
    ls = [arr[i] for i in range(len(arr) - 1) if arr[i] != arr[i + 1]]
    ls.append(arr[-1])
    return ls
print(solution2([1,1,3,3,0,1,1]))
print(solution2([4,4,4,3,3]))

# 아이디어
# 반복되는 숫자 제거하기1 => 원소의 크기가 바뀌는 순간 해당 원소를 리스트에 저장 => 별도 리스트에 append 또는 리스트 컴프리헨션
# 그리고 마지막 원소도 저장 => append
# 정리 => 어떤 리스트에서 일정한 특징을 갖는 원소들로 또 다른 리스트를 만든다면 리스트 컴프리헨션이 적합함
# 반복되는 숫자 제거하기2 
# => 원소를 한 번만 저장하기 위한 별도 리스트 만들고 
# => 그 리스트의 원소와 비교하면서 같다면 continue(건너뛰기) 다르다면 추가
# [-1]을 통해 비교하면 empty array일 때 인덱싱오류가나서 
# [-1:]를 통해 리스트를 만들어 비교하는 군요. 잘 배워갑니다.
