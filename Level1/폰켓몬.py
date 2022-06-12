def solution(nums):
    l = len(set(nums))
    n = len(nums) // 2
    if l <= n:
        return l
    else:
        return n
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

# 아이디어
# 폰켓몬이 몇 종류 있는지 => len(set(nums))
# len(nums) // 2 마리를 최대한 많은 종류를 선택해서 뽑아야 됨
# => set(nums) 집합 => 모든 종류를 뽑아놓은 것과 같음
# => 따라서 set(nums)에서 len(nums) // 2 마리만큼 되게 만들면 됨

# 예제 로직을 이해하고 흐름을 따라서 규칙을 찾고 식을 세우는 문제