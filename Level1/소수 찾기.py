def solution1(n):
    answer = 0
    for num in range(1, n + 1):
        cnt = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                cnt += 1
        cnt += 1
        if cnt == 2:
            answer += 1
    return answer
print(solution1(10))

def solution2(n):
    arr = [False, False] + [True] * (n - 1)
    primes = []
    cnt = 0

    for i in range(2, n + 1):
        if arr[i]:
            cnt += 1
            for j in range(i * 2, n + 1, i):
                arr[j] = False
    print(arr)
    return cnt
print(solution2(10))

def solution3(n):
    primes = set(range(2, n + 1))
    for i in range(2, n + 1):
        primes = primes - set(range(i * 2, n + 1, i))
    return len(primes)
print(solution3(10))

아이디어
소수 찾기1 => 1부터 n까지 반복하면서 이중 for문으로 다시 1부터 해당수까지 반복하며 해당 수를 나눠을 때 나머지가 0인 것을 찾음 => 시간복잡도 문제 생김
소수 찾기2 => 에라토스테네스의 체 : 2, 3, 4, ..... 에서 2의 배수 제거, 3의 배수 제거, ....
소수인 수 => True로 저장
소수 아닌 수 제거 => False로 바꿈
소수 찾기3 => 에라토스테네스의 체 : 어떤 수의 배수 제거 => 집합 사용(차집합)