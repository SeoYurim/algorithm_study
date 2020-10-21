# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42748

# 정렬

## map 써야될거같았는데 정확하게 어떻게 쓸지 몰라서 그냥 푼 문제

# 나의 풀이
## 그냥 나와있는 대로...
### 자르고 정렬해서 k번째수 찾아낸다.
def solution(array, commands):
  answer = []
  slice_array = []
  for i in commands:
    slice_array = array[i[0]-1:i[1]]
    slice_array.sort()
    answer.append(slice_array[i[2]-1])
  return answer


# 다른사람 풀이
## map, lamda ... 공부해야겠다 진짜..
def solution(array, commands):
  return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

