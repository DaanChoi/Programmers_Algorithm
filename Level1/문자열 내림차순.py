def solution1(s):
    return ''.join(sorted(s, reverse=True))
print(solution1("Zbcdefg"))

# 아이디어
# 문자열 정렬 => sorted() 사용 : 문자열 정렬 후 리스트로 반환함 -> join으로 다시 문자열 만들어줌
# sort()는 문자열은 안됨, 리스트만 됨
