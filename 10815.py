N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

for i in range(M):
  ans = 0
  l = 0
  r = N-1
  mid = (l+r)//2

  while(l<=r):
    if A[mid] == B[i]:
      ans = 1
      break
    elif A[mid] < B[i]:
      l = mid + 1
    else:
      r = mid - 1
    mid = (l+r)//2
  print(ans, end=' ')

# end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨