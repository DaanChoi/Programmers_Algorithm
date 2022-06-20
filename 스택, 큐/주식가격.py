# 아이디어
# 1. 이중반복문 => O(n2)
# 2. 스택 => O(n)

#이중반복문
def solution1(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(len(prices) - 1 - i)
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
    return answer
print(solution1([1,2,3,2,3]))
print(solution1([1,2,5,3,1]))

#스택
def solution2(prices):
    n = len(prices)
    answer = [0 for i in range(n)]
    stack = [] # 주식이 앞으로 떨어질 수도 있지만 떨어지지 않은 시간(인덱스)의 모음

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]: # 마지막으로 주식이 떨어지지 않은 시간의 주식 가격과 계속 비교
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = n - top - 1
    return answer
print(solution2([1,2,3,2,3]))
print(solution2([1,2,5,3,1]))

# 이해하는데 오래걸림.. 앞으로 이 방법을 응용할 수 있을지..
# 반복 학습만이 방법이다
# https://www.youtube.com/watch?v=PhB6fIJAH5A 이해하는데 이 영상이 도움됨
