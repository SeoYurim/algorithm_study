# 문제
# 트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

# 트리가 주어졌을 때, 노드 중 하나를 제거할 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다.
# 셋째 줄에는 지울 노드의 번호가 주어진다.
# =======================================================================================================================

# 문제 해결 순서
1. 입력받기(node의 개수, 각각 노드의 부모 노드, 지울 노드 번호)
2. tree 생성하기
2 - 1. Node class안에 setChild와 removeChild 함수를 정의하여 tree를 생성하고 node를 지우는데 편리하게 한다.

# 입력받기
node_count = int(input())
parent = list(map(int, input().split()))
node_num = int(input())


class Node:
    def __init__(self):
        self.child = []

    def setChild(self, node):
        self.child.append(node)

    def removeChild(self, node):
        self.child.remove(node)


tree = [Node() for _ in range(node_count)]
cnt = 0


def preorder(node):
    global cnt
    if node.child == []:
        cnt += 1
    for child in node.child:
        preorder(tree[child])


for i in range(node_count):
    if parent[i] != -1:
        tree[parent[i]].setChild(i)

if node_count != 1:
    if parent[node_num] == -1:
        cnt = 0
    else:
        tree[parent[i]].removeChild(i)
        preorder(tree[parent.index(-1)])

print(cnt)
