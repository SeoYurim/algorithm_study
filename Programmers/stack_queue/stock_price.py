def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer


print(solution([2, 3, 4, 5, 3, 2, 3]))
print(solution([2, 3, 4, 5, 6]))
# , [4, 3, 1, 1, 0]
