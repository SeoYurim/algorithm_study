# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42747

# sort
# 조금 이해하기 어려웠던 문제

# 나의 풀이
## h의 최댓값은 배열의 길이
## answer을 0으로 선언해 놓고 마지막에 answer을 출력하니 에러가 났다.

def solution(citations):
  citations.sort()
  l = len(citations)
  
  for i in range(l):
    if citations[i] >= l-i:
        # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
        return l-i   
  return 0

# 다른 사람 풀이
## enumerate

def solution(citations):
  citations.sort(reverse=True)
  answer = max(map(min, enumerate(citations, start=1)))
  return answer