def solution1(array, commands):
    answer = []
    for command in commands:
        ls = [array[i] for i in range(command[0] - 1, command[1])]
        ls.sort()
        answer.append(ls[command[2] - 1])
    return answer
print(solution1([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

def solution2(array, commands):
    answer = []
    for command in commands:
        i, j, k = command # i = command[0] / j = command[1] / k = command[2]
        answer.append(sorted(array[i - 1:j])[k - 1])
    return answer 
print(solution2([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# i, j, k, l = ls
# 배열의 각 원소를 변수에 담기(언팩킹)
