# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42578
# hash

# my solution
import collections

def solution(clothes):
    answer = 1
    category = list()

    for i in range(len(clothes)):
        category.append(clothes[i][1])
    
    categories = collections.Counter(category)
    
    count_list = list(categories.values())
    
    for i in count_list:
        answer *= i+1
    answer = answer -1
    return answer

# 같은 카테고리 별로 분류 하여 그 개수를 센다. => Counter함수 사용
# Counter함수를 활용하면 결과가 dictionary로 나오는데, 여기서 개수를 나타내는 value값만 따로 list로 저장
# (개수+1)해서 모두 곱한 뒤 -1을 해준다.

# 하나의 카테고리에서 발생하는 경우의 수는 (n개+1) => 1은 안입을 경우

### 다른사람들 풀이

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

# 사용한 함수 : Counter, reduce
# reduce + lambda
## 1. lambda : 익명함수
## 2. reduce : 여러개의 데이터를 대상으로 주로 누적 집계를 내기 위해 사용
###  사용방법 : reduce(집계 함수, 순회 가능한 데이터[, 초기값])