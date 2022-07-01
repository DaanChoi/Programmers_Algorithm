def solution1(answers):
    patterns1 = [1, 2, 3, 4, 5]
    patterns2 = [2, 1, 2, 3, 2, 4, 2, 5]
    patterns3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    submit1 = []
    submit2 = []
    submit3 = []

    submit1 = patterns1 * (len(answers) // len(patterns1)) + patterns1[0:len(answers) % len(patterns1)]
    submit2 = patterns2 * (len(answers) // len(patterns2)) + patterns2[0:len(answers) % len(patterns2)]
    submit3 = patterns3 * (len(answers) // len(patterns3)) + patterns3[0:len(answers) % len(patterns3)]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(len(answers)):
        if answers[i] == submit1[i]:
            cnt1 += 1
        if answers[i] == submit2[i]:
            cnt2 += 1
        if answers[i] == submit3[i]:
            cnt3 += 1    
    
    correct = [cnt1, cnt2, cnt3]

    return [i + 1 for i in range(len(correct)) if correct[i] == max(correct)]
print(solution1([1,2,3,4,5]))
print(solution1([1,3,2,4,2]))

def solution2(answers):
    patterns1 = [1, 2, 3, 4, 5]
    patterns2 = [2, 1, 2, 3, 2, 4, 2, 5]
    patterns3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for i, answer in enumerate(answers):
        if answer == patterns1[i % len(patterns1)]:
            scores[0] += 1
        if answer == patterns2[i % len(patterns2)]:
            scores[1] += 1
        if answer == patterns3[i % len(patterns3)]:
            scores[2] += 1

    return [i + 1 for i in range(len(scores)) if scores[i] == max(scores)]
print(solution2([1,2,3,4,5]))
print(solution2([1,3,2,4,2]))

# 아이디어
# 1
# 각 학생의 정답 패턴 리스트를 answer 리스트 크기랑 같게 만들어 줌
# 그리고나서 반복문으로 정답 갯수 확인
# 가장 많이 맞은 학생 갯수 찾고 그 학생 반환

# 2
# 패턴 리스트 인덱싱에 %나머지 연산을 이용
# for문에 enumerate 사용해서 인덱스와 원소 돌림
