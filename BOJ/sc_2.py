import math


def is_int(x):
    if int(x) == x:
        return True
    else:
        return False


def solution(n):
    answer = 0
    log_n = math.log2(n)
    x = int(math.floor(log_n))
    if is_int(log_n):
        answer += 3 ** log_n
        return int(answer)
    else:
        p = 3 ** x
        return p + solution(n-2**x)


print(solution(11))
