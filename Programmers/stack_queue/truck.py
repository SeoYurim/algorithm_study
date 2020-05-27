# from collections import deque


# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     queue = deque(truck_weights)

#     on_bridge = deque([0] * bridge_length)

#     while queue:
#         answer += 1
#         on_bridge.popleft()
#         if sum(on_bridge) + queue[0] > weight:
#             on_bridge.append(0)
#         else:
#             on_bridge.append(queue.popleft())
#     answer += bridge_length
#     return answer
# sum()은 O(N) 이라서 시간초과 났던 문제
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)

    on_bridge = deque([0] * bridge_length)
    total_weight = 0

    while queue:
        answer += 1
        total_weight -= on_bridge[0]
        on_bridge.popleft()
        if total_weight + queue[0] > weight:
            on_bridge.append(0)
        else:
            on_bridge.append(queue.popleft())
            total_weight += on_bridge[-1]
    answer += bridge_length
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
