# https://velog.io/@inyong_pang/%ED%95%B4%EC%89%AC-%ED%85%8C%EC%9D%B4%EB%B8%94Hash-Table
# https://coding-grandpa.tistory.com/85

# 아이디어
# 1. 반복문
# 2. 해시 딕셔너리

def solution1(participant, completion):
    for a in completion: 
        participant.remove(a)
    return participant[0]
print(solution1(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution1(["leo", "kiki", "eden"], ["eden", "kiki"]))
# 시간복잡도 O(n2) => 효율설 테스트 탈락

def solution2(participant, completion):
    hashDict = {}
    sumKey = 0
    for value in participant:
        hashDict[hash(value)] = value
        sumKey += hash(value)

    for c in completion:
        sumKey -= hash(c)
    
    return hashDict[sumKey]
print(solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution2(["leo", "kiki", "eden"], ["eden", "kiki"]))
# 해시값을(hash()) 사용하지 않더라도 직접 key값을 임의로 지정해줘서 그냥 딕션너리 문제로 풀어도 됨
# 해시의 시간복잡도 O(n)
# 통과하지 못한 한 사람 , 범인, 등등과 같은 두 그룹 중 차이점 하나 찾기 문제 유형에서 써보기
# 각 원소를 식별할 필요가 있을 때 해시 써보기
