# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42746

# 정렬

# 문제 조건을 잘 읽자!

def solution(numbers):
  numbers = [str(x) for x in numbers]
  numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
  answer = "".join(numbers) if numbers[0] != "0" else "0"
  return answer

# numbers의 원소들이 3자리수 이하
# 1. numbers를 문자열로 치환한다.
# 2. 각 원소를 "무수히 많이 반복하여 길이를 4로 자른 문자열" 기준으로 numbers를 정렬합니다.
# 3. 문자열을 합쳐줍니다.