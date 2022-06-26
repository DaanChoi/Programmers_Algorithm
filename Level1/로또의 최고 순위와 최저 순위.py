def solution(lottos, win_nums):
    answer = []

    rank = [6, 5, 4, 3, 2]
    cnt = 0
    zero = 0

    for n in lottos:
        if n in win_nums:
            cnt += 1
        elif n == 0:
            zero += 1
    
    best = cnt + zero
    worst = cnt

    if best >= 2:
        answer.append(rank.index(best) + 1)
    else:
        answer.append(6)
    
    if worst >= 2:
        answer.append(rank.index(worst) + 1)
    else:
        answer.append(6)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

# 아이디어
# 단순 구현 문제였음
# 문제의 조건에 따라 그대로 코드에 옮기면 됐음
# 0의 개수에 따라 최고일 때와 최저일 때가 결정되기 때문에 0의 개수를 잘 처리하는 게 주요했고
# 당첨번호 개수에 따른 rank 결정을 위해 => rank 리스트를 따로 만들고 인덱스 + 1을 순위로 사용함
# 순위 결정을 위한 조건 세우기가 살짝 복잡했음
