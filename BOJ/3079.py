N, M = map(int, input().split())

times = []
for i in range(N):
    time = int(input())
    times.append(time)

left = 1
right = min(times)*M
result  = right
while(left < right):
    mid = (left+right)//2
    people = 0
    for i in range(N):
        people += mid//times[i]

    if people >= M:
        right = mid
    else: 
        left = mid + 1
print(left)