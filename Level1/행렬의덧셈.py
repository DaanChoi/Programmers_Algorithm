def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            arr1[i][j] += arr2[i][j]
    return arr1
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))

#아이디어
#행렬이 이차원 리스트이기 때문에 이중 for문으로 인덱싱
