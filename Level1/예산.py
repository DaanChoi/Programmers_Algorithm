def solution(d, budget):
    sum = 0
    cnt = 0
    for x in sorted(d):
        sum += x
        if sum > budget:
            break
        cnt += 1
    return cnt
print(solution([1,3,2,5,4],	9))
print(solution([2,2,3,3], 10))

# 아이디어
# 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없고
# 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 함
# => 예산 작은 것부터 예산에 포함시키면 최대한 많은 부서를 지원해줄 수 있음
# => 각 부서별 신청 금액 리스트(d)를 오름차순으로 정렬
