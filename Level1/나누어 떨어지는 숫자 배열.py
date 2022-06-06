def solution(arr, divisor):
    ls = [i for i in arr if i % divisor == 0]
    return sorted(ls) if len(ls) != 0 else [-1]
print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))

# 아이디어
# arr의 각 원소 중(for문) divisor로 나눠 떨어지는 수로(if문) 이뤄진 리스트 만들기(리스트 컴프리헨션)
