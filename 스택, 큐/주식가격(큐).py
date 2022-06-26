#[1,2,3,2,3]
for i in []:
    print("hello")

from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft() # 1, 2, 3, 2, 3
        sec = 0
        for q in queue: # 
            sec += 1 # 1, 2, 3, 4 / 1, 2, 3 / 1 / 1 / queue 비워있으므로 for문 실행 안됨(에러는 아님)
            if price > q: # / / 3 > 2
                break
        answer.append(sec) # [4, 3, 1. 1, 0]
    return answer
print(solution([1,2,3,2,3]))

# 아이디어
# 인덱스가 0인 시점부터 가격이 떨어질 때까지의 초를 세고,
# 인덱스가 1인 시점부터 가격이 떨어질 때까지의 초를 세고,
# 이 과정을 모든 인덱스에 반복하는 것이다.
# 이 문제는 스택보다 큐가 더 적합한 것 같음, 직관적이고, 문제 논리와 코드 매칭이 잘 됨.
