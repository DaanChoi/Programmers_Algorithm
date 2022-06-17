def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for num in reserve_set:
        if (num - 1) in lost_set:
            lost_set.remove(num - 1)
        elif (num + 1) in lost_set:
            lost_set.remove(num + 1)

    return n - len(lost_set) 
print(solution(5, [2, 4], [1, 3, 5]))

# 아이디어
# 체육복 있는 학생 집합과 체육복 여벌이 있는 학생 집합으로 나눠짐
# 문제 조건에 여러 집합이 나온다면 => 집합 활용 생각해보기
