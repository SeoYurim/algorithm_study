# 문제
# 세준이는 N*N크기의 배열을 만들었다. (배열의 방 번호는 1부터 시작한다.)

# 그 배열을 A라고 했을 때, 배열에 들어가는 수는 A[i][j] = i*j 이다.

# 세준이는 이 수를 일차원 배열 B에 넣으려고 한다. 그렇게 되면, B의 크기는 N*N이 될 것이다. 그러고 난 후에, B를 오름차순 정렬해서 k번째 원소를 구하려고 한다.

# N이 주어졌을 때, k번째 원소를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(109, n2)보다 작거나 같은 자연수이다.

# 출력
# k번째 원소를 출력한다.

N = int(input())
k = int(input())

left = 1 
right = k
ans = 0

while left <= right:
  count = 0
  mid = (left+right)//2
  
  for i in range(1, N+1):
    count += min(mid//i, N)
  if(count < k):
    left = mid + 1
  else:
    ans = mid
    right = mid -1
print(ans)