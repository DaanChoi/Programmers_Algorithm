def solution(sizes):
    width = [min(a) for a in sizes]
    height = [max(a) for a in sizes]
    return max(width) * max(height)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

# 아이디어
# 적절히 회전시킴 => width 리스트 에는 작은 수 몰아놓고 height 리스트에는 큰 수 몰아놓음
# result => width 중 가장 큰 수 곱하기 height 중 가장 큰 수 만들기
