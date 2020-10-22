# algorithm_study
[Algorithm] coding test 준비하기

### Day001 
#### [PROGRAMMERS] 해시 : 전화번호 목록(python)

* sort() 활용해서 접두어가 같은 숫자끼리 및 문자열 길이로 정렬 후 비교
* 똑똑한 사람들이 많은거 같다,,
* 문제 : https://programmers.co.kr/learn/courses/30/lessons/42577


### Day001 
#### [PROGRAMMERS] 해시 : 완주하지 못한 사람(python)

* 처음에 이중 for문으로 하니까 효율성 통과 못함
* hash / dict 활용
* Counter => 중복되는 단어 개수 찾을 때 활용
* 문제 : https://programmers.co.kr/learn/courses/30/lessons/42576


### Day002
#### [PROGRAMMERS] 해시 : 위장(python)

* 같은 카테고리끼리 묶고 경우의 수를 생각하기
* lambda : 익명함수
* reduce() : 여러개의 데이터를 대상으로 주로 누적 집계를 내기 위해 사용

`reduce(집계 함수, 순회 가능한 데이터[, 초기값])`

```python
reduce(lambda x, y: x*(y+1), cnt.values(), 1)
```
* 문제 : https://programmers.co.kr/learn/courses/30/lessons/42578


### Day003
#### [PROGRAMMERS] 힙 : 더 맵게(python)

* python의 heapq모듈을 활용하여 heap을 만들기
* heapq.heapify() => heap으로 만들어 준다
* heapq.heappop() => 가장 우선순위가 높은 노드(=가장 작은 노드) 삭제

* 문제 : https://programmers.co.kr/learn/courses/30/lessons/42626


### Day004
#### [PROGRAMMERS] 정렬 : K번째 수(python) level1

* map과 sort를 활용하면 한줄로 끝나는 문제
* map이나 reduce 등 간단하게 쓸 수 있는 함수에 대해 더 공부해야 될 것 같다.
* map 함수 활용

`list(map(함수, 리스트))`
* 예시)
```python
## 실수로 구성된 리스트의 요소들을 정수로 변환
## float -> int
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
  a[i] = int(a[i])
```
map함수를 활용하면 더 간단해집니다.

```python
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
```
* 문제 : https://programmers.co.kr/learn/courses/30/lessons/42748

### Day005
#### [PROGRAMMERS] 정렬 : 가장 큰 수(python) level2

* map, lambda 써서 해결한 문제
* 문제의 조건을 잘 읽고 해결할 수 있는 방법을 찾기
* numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
* x*4[:4]를 기준으로 정렬 => key활용

* 문제 : https://programmers.co.kr/learn/courses/30/lessons/42746
