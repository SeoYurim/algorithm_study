# 그래프

- 정점과 간선으로 이루어진 자료구조의 일종 C = (V,E)

# 그래프 탐색

* 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것

ex) 특정 도시에서 다른 도시로 갈 수 있는지 없는지, 전자 회로에서 특정 단자와 단자가 서로 연결되어 있는지

# 깊이 우선 탐색 (DFS - Depth First Search)

* 루트노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법

1. 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 이곳으로부터 다른 방햐으로 다시 탐색을 진행하는 방법과 유사

2. 즉 넓게(wide) 탐색하기 전에 깊게(deep) 탐색함

3. 모든 노드를 방문하고자 하는 경우에 이 방법을 선택함

4. BFS(너비 우선 탐색)보다 더 간단함

5. 검색속도 자체는 BFS보다 느림

## DFS의 특징

* 자기 자신을 호출하는 **순환 알고리즘**의 형태를 지님
* 이 알고리즘을 구현할 때 가장 큰 차이점은 그래프 탐색의 경우 **어떤 노드를 방문**했었는지 여부를 반드시 검사해야한다는 것 (이를 검사하지 않을 경우 무한루프에 빠질 위험이 있다.)

![DFS](https://t1.daumcdn.net/cfile/tistory/9983A7335BD0156910?download “DFS”)

* 깊이 우선 탐색(DFS)의 시간 복잡도
  * DFS는 그래프의 모든 간선을 조회함 (정점의 수: N, 간선의 수: E)
    * 인접 리스트로 표현된 그래프 : O(N+E)
    * 인접 행렬로 표현된 그래프 : O(N^2)

# 너비 우선 탐색(BFS - Breadth First Search)

* 루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법

1. 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법

2. 깊게(deep)탐색하기 전에 넓게(wide) 탐색하는 것

3. 두 노드 사이의 **최단 경로** 혹은 **임의의 경로**를 찾고 싶을 때 이 방법을 선택함

## 너비우선탐색(BFS)의 특징
* BFS는 **재귀적으로 동작하지 않는다**
* 이 알고리즘을 구현할 때 가장 큰 차이점은 그래프 탐색의 경우 **어떤 노드를 방문**했었는지 여부를 반드시 검사해야한다는 것이다. 이를 검사하지 않을 경우 무한 루프에 빠질 위험이 있다.
* BFS는 방문한 노드들을 차례로 저장한 후 꺼낼 수 있는 자료구조 Queue를 사용한다 => FIFO

![BFS](https://t1.daumcdn.net/cfile/tistory/99960F405BD01A8D18?download “BFS”)

## DFS vs BFS

ex) 지구 상에 존자하는 모든 친구 관계를 그래프로 표현한 후 Ash와 Vanessa 사이에 존재하는 모든 경로를 찾는 경우

* 깊이우선탐색(DFS) => 모든 친구 관계를 다 살펴봐야할지도 모른다

* 너비 우선탐색(BFS) => Ash와 가까운 관계부터 탐색

`너비우선`은 한 단계씩 가능한 모든 경우의 수를 확인

`깊이우선`은 한 우물만 파고들며 가능한 수가 나올 때까지 확인


![differ] (https://t1.daumcdn.net/cfile/tistory/997C3C3E5BD01AF41D "differ")

## DFS와 BFS 구현하기

DFS는 `스택(stack)`을 사용한다
* pop : 스택의 맨 위 노드를 꺼내는 일
* expand : pop으로 노드를 지우면서 그 노드의 **자식**을 모두 스택에 넣는 일
BFS는 `큐(queue)`를 사용한다

인접행렬 / 인접리스트

* 인접행렬 => O(v^2)
* 인접행렬 => O(V+E)

=> 인접행렬보다는 인접리스트가 더 효율적이다.

### DFS

* stack 이용

```python
def DFS(start_node):
  # 1) stack에 첫번째 노드를 넣으면서 시작
  stack = [start_node]

  while True:
    # 2) stack이 비어있는지 확인
    if len(stack) == 0:
      print('All node searched')
      return None

    # 3) stack에서 맨 위의 노드를 pop
    node = stack.pop()

    # 4) 만약 node가 찾고자 하는 target이라면 서치 중단
    if node == TARGET:
      print('The target found')
      return node

    #5) node의 자식을 expand해서 children에 저장함
    children = expand(node)

    # 6) children을 stack에 쌓기
    stack.extend(children)

    # 7) 이렇게 target을 찾거나, 전부 탐색해서 stack이 빌 때까지 while문 반복
```

### BFS

* queue 이용
  * dequeue : 큐에서 맨 앞에 있는 노드를 꺼내는 일
  * expand : dequeue로 노드를 지우면서 그 노드의 자식을 모두 큐에 넣는 일

```python
def BFS(start_node):
    	# 1) queue 에 첫 번째 노드 넣으면서 시작
        queue = [start_node, ]
        
        while True:
            # 2) queue가 비어있는지 확인 
            if len(queue) == 0:
            	print('All node searched.')
                return None
                
            # 3) queue에서 맨 앞의 노드 를 dequeue (0번 인덱스를 pop)
            node = queue.pop(0)
                
            # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
            if node == TARGET:
            	print('The target found.')
                return node
            
            # 5) node의 자식을 expand 해서 children에 저장
            children = expand(node)
            
            # 6) children을 stack에 쌓기
            queue.extend(children)
            
            # 7) 이렇게 target을 찾거나, 전부 탐색해서 queue가 빌 때까지 while문 반복
```
https://jeinalog.tistory.com/entry/Python-DFS-BFS-A-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%BF%8C%EC%8B%9C%EA%B8%B0-feat-%ED%8D%BC%EC%A6%90-%EB%AF%B8%EB%A1%9C