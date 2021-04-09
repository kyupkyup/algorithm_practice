from _collections import deque

n = int(input())
arr_node = list(map(int, input().split(" ")))
delete = int(input())



class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = []

    def find(self, root, value):
        node = None
        def recur(curr):
            nonlocal node
            if curr.value == value:
                node = curr
                return

            for i in curr.child:
                recur(i)

        recur(root)
        return node

def solution():

    val_nodes = []
    for value, node in enumerate(arr_node):
        val_nodes.append(Node(value, node))

    for i in val_nodes:
        for j in val_nodes:
            if i.value == j.parent:
                i.child.append(j)

    val_nodes = sorted(val_nodes, key=lambda x : x.parent) # 부모노드 기준으로 정렬
    for i in val_nodes:
        if i.value == delete: # 지울 노드 찾기
            if i.parent == -1: # 루트 노드면 그냥 0 출력 후 리턴
                print(0)
                return

            children = i.find(val_nodes[0], i.parent).child # 부모에서 자식 노드를 끊어줘야 하기 떄문에 root부터 내려와서 지워줌
            if not children:
                break
            else:
                children.remove(i)

    count = 0 #
    dq = deque([])
    dq.append(val_nodes[0])
    while dq:
        node = dq.popleft()
        if not node.child:
            count += 1
        else:
            for i in node.child: #자식 노드 없는거 bfs 로 찾아줌
                dq.append(i)
    print(count)

solution()