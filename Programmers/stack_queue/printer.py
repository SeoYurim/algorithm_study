def solution(priorities, location):
    answer = 0
    prin = []
    idx_list = [(p, i) for i, p in enumerate(priorities)]
    while idx_list:
        x = idx_list.pop(0)
        x_num = x[0]
        x_idx = x[1]
        m = max(priorities)

        if x_num == m:
            priorities.remove(m)
            prin.append(x_idx)
        else:
            idx_list.append(x)

    answer = prin.index(location) + 1

    return answer


print(solution([2, 1, 3, 2], 2))

print(solution([1, 1, 9, 1, 1, 1], 0))
