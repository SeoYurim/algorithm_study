N = int(input())
A = list(map(int, input("A의 배열을 입력하세요").split()))
B = list(map(int, input("B의 배열을 입력하세요").split()))
S = 0

for i in range(N):
  S += min(A)*max(B)
  A.remove(min(A))
  B.remove(max(B))

print(S)


