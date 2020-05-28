from collections import deque
import math


def solution(progresses, speeds):
    answer = []

    days = deque([0] * len(progresses))

    for i in range(len(progresses)):
        left = 100 - progresses[i]
        days[i] = math.ceil(left / speeds[i])

    while days:
        count = 1

        a = days.popleft()

        for _ in range(len(days)):

            if days[0] <= a:
                count += 1
                days.popleft()
            else:

                break

        answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]))
print(solution([93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7]))
