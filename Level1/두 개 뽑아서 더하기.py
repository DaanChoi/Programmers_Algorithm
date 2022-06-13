def solution(numbers):
    result = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            result.append(numbers[i] + numbers[j])
    return sorted(list(set(result)))
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

# 아이디어
# 서로 다른 인덱스의 두 원소 뽑기 => 선택정렬과 비슷한 원리로 반복문 범위 설정 => 앞에서부터 범위를 좁혀가며
# 중복 제거 => set()
# set()는 자동으로 오름차순 정렬을 해주는 것처럼 보이지만 자동으로 오름차순 정렬을 해주지 않는다함..
