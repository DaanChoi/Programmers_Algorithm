# 아이디어
# 1. 스택 사용
# 2. 힙 사용

def solution1(scoville, k):
    cnt = 0
    scoville = sorted(scoville, reverse = True)
    while scoville[-1] < k:
        if len(scoville) > 1:
            num1 = scoville.pop()
            num2 = scoville.pop()
            scoville.append(num1 + num2 * 2)
            scoville = sorted(scoville, reverse = True)                 
            cnt += 1
        else:
            return -1
    return cnt
print(solution1([1, 2, 3, 9, 10, 12], 7))
# 스택 사용 => 효율성 테스트 탈락

def solution2(scoville, k):
    import heapq

    cnt = 0
    heapq.heapify(scoville) # 기존의 리스트를 오름차순 heapQ로 변환
    while scoville[0] < k:
        if len(scoville) > 1:
            num1 = heapq.heappop(scoville) # list의 가장 작은 값을 return하며 삭제
            num2 = heapq.heappop(scoville)
            heapq.heappush(scoville, num1 + num2 * 2) # list에 값을 삽입, 자동으로 정렬한다
            cnt += 1
        else:
            return -1
    return cnt
print(solution2([1, 2, 3, 9, 10, 12], 7))

# 힙 => 효율성 테스트 통과
# heap은 최소 값이나 최대 값을 찾기 위해 고안된 트리 형식의 자료 구조이다.
# 데이터의 삽입, 반환 시 전체를 다시 sort 할 필요 없이 자료 구조 알고리즘을 통해 정렬된다.
# Python의 heapQ는 min-heap(부모 노드가 자식 노드의 값 보다 작음)이며, max-heap을 위해서는 별도의 처리가 필요하다.
# pop, push, 리스트에서 변환시에는 자동으로 배열이 정렬되는 특징이 있다.
