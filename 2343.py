N, M = input().split()
record = list(map(int, input().split()))

N = int(N)
M = int(M)

left = 0
right = 0

for i in range(N):
    right += record[i]
    left = max(left, record[i])

while (left <= right):
    mid = (left+right)//2
    sum = 0
    cnt = 0
    for i in range(N):
        if(sum + record[i] > mid):
            sum = 0
            cnt += 1
        sum += record[i]
    
    if (sum != 0):
        cnt += 1
    if (cnt <= M):
        right = mid - 1
    else:
        left = mid + 1
print(left)
