# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer.keys())[0]

# collections.Counter 모듈 활용
# 중복되는 단어 찾기 할 때 많이 사용한다.
# dict 형식으로 return
# 객체들 사이의 연산 가능

# code2
# hash() 활용

# code3
# sort()해서 빼기

