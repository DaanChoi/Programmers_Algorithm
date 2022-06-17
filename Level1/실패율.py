def solution(n, stages):
    fail = []
    people = len(stages)
    for i in range(1, n + 1):
        if people != 0:
            cnt = 0
            for s in stages:
                if s == i:
                    cnt += 1
            fail.append([i, cnt/people])
            people -= cnt
        else:
            fail.append([i, 0])
    fail = sorted(fail, reverse = True, key = lambda x: x[1])
    return [fail[i][0] for i in range(i)]
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# 아이디어
# 실패율 = 실패 인원 / 인원 수 => 실패 인원을 세고, 실패 인원을 분자에 쓰고, 다음 스테이지에서는 실패 인원만큼 분모에 빼줌
# ref) https://dailylifeofdeveloper.tistory.com/245
# def solution(n, stages):
#     fail = []
#     people = len(stages)
#     for i in range(1, n + 1):
#         if people != 0:
#             cnt = 0
#             for s in stages:
#                 if s == i:
#                     cnt += 1
#             fail.append([i, cnt/people])
#             people -= cnt
#         else:
#             fail.append([i, 0])
#     fail = sorted(fail, reverse = True, key = lambda x: x[1])
#     return [fail[i][0] for i in range(i)]
# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# 런타임에러 이유 추측
# people 참가자 수가 0이 되는 경우가 생김

# 이차원 리스트를 세팅 해놓지 않고
# 그냥 리스트에서 ls.append([x, y])으로 추가하는 것도 있음
