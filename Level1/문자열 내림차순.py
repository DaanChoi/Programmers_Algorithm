def solution1(s):
    return ''.join(sorted(s, reverse=True))
print(solution1("Zbcdefg"))

def solution2(s):
    s.sort()
    return ''.join(s)
print(solution2("Zbcdefg"))