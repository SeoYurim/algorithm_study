# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42626

# heap
## heap: 특정 규칙을 갖는 트리 => 우선순위 큐
# python 에는 heapq라는 모듈이 존재
# heapq.heapify() => heap으로 만들어 준다.

# heap 만들기
# 1. 들어오는 원소를 트리의 가장 아래에 배치
# 2. 부모노드와 비교하여 새로 들어온 값이 더 작으면 부모를 아래로 내리고 새로들어온 노드가 위로

# heappop() => 가장 작은 원소 삭제

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        if a < K:
            new_K = a + b * 2
            answer += 1
            heapq.heappush(scoville, new_K)

        else:
            return answer
            break

    if scoville[0] < K:
        return - 1
    else:
        return answer