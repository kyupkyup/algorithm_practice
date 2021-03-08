class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head

        while True:
            if value < self.current_node.value:
                # 현재 포인트하는 노드의 값보다 받아온 값이 작으면 = 왼쪽으로 가야함
                if self.current_node.left != None:
                    # 왼쪽이 비지 않았으면
                    self.current_node = self.current_node.left
                    #왼쪽 노드로 이동
                else:
                    #왼쪽이 비었으면
                    self.current_node.left = Node(value)
                    break
                    # 왼쪽에 노드 추가
            else:
                # 현재 포인트하는 노드의 값보다 받아온 값이 크면 = 오른쪽으로 가야함
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        # value를 찾았을 경우
        if not searched:
            return False
        else:
        #case1  child 노드가 없는 노드 삭제 경우
            if self.current_node.left == None and self.current_node.right == None:
                if value < self.parent.value:
                    self.parent.left = None
                else:
                    self.parent.right = None
                del self.current_node
        #case2 child 노드가 하나 있는 삭제 경우

            if self.current_node.left != None and self.current_node.right == None:
                # case2-1 child 노드가 하나 있는데 왼쪽일 경우
                if value < self.parent.value:
                    # 지우려는 노드가 부모 노드의 왼쪽에 있는 경우
                    self.parent.left = self.current_node.left
                    # 현재 노드의 왼쪽 노드를 부모의 왼쪽에 붙여줌
                else:
                    # 지우려는 노드가 부모 노드의 오른쪽에 있는 경우
                    self.parent.right = self.current_node.left
                    # 현재 노드의 왼쪽 노드를 부모의 오른쪽에 붙여줌

            elif self.current_node.left == None and self.current_node.right != None:
                #case2-2 child 노드가 하나 있는데 오른쪽일 경우
                if value < self.parent.value:
                    self.parent.left = self.current_node.right
                else:
                    self.parent.right = self.current_node.right

            if self.current_node.left != None and self.current_node.right != None:
                # case3 child 노드가 두 개 모두가 있을 경우
                if value < self.parent.left:
                    # case3-1 삭제할 노드(current_node)가 parent의 왼쪽에 있는 경우
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.parent
                    while self.change_node.left != None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                    # 삭제할 노드 아래의 왼쪽에 노드가 없을 때 까지 노드를 타고 내려감
                    if self.change_node.right != None:
                        # 왼쪽 노드가 없는 노드에 도착했을 때, 오른쪽 노드가 있는 경우
                        self.change_node_parent.left = self.change_node.right
                        # 오른쪽 노드를 그대로 바꾸는 노드의 왼쪽에 갖다 붙임
                    else:
                        self.change_node_parent.left = None
                        # 오른쪽 노드가 없으면 그냥 비워 버림
                    self.parent.right = self.change_node
                    # 삭제 노드의 부모의 오른쪽에 바꿀 노드를 갖다붙임
                    self.change_node.left = self.current_node.left
                    # 바꿀 노드의 왼쪽에 삭제 노드의 왼쪽을 갖다 붙이고
                    self.change_node.right = self.current_node.right
                    # 바꿀 노드의 오른쪽에 삭제노드의 오른쪽을 갖다 붙임
        return True


import random

# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print (bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)







