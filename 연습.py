class n




def insert(self, value):
    if self.root is None:
        self.root = Node(value)
    else:
        curr = self.root
        while curr is not None:
            if value == curr.value:
                print("already there is node")
                return False

            elif value > curr.value:
                if curr.right is None:
                    curr.right = Node(value)
                    return
                curr = curr.right
            elif value < curr.value:
                if curr.left is None:
                    curr.left = Node(value)
                    return
                curr = curr.left




















class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            curr = self.root
            while curr is not None:
                if value == curr.value:
                    print("already there is node")
                    return False

                elif value > curr.value:
                    if curr.right is None:
                        curr.right = Node(value)
                        return
                    curr = curr.right
                elif value < curr.value:
                    if curr.left is None:
                        curr.left = Node(value)
                        return
                    curr = curr.left

    def search(self, value):
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return curr
            if value > curr.value:
                curr = curr.right
            else:
                curr = curr.left
        return False

    def remove(self, value):
        parent = None
        direction = "l"
        isHere = False
        curr = self.root
        while curr is not None:
            if value == curr.value:
                isHere = True
                break
            parent = curr
            if value > curr.value:
                direction = "r"
                curr = curr.right
            else:
                direction = "l"
                curr = curr.left

        if not isHere:
            return False

        # 하위 노드가 없는 경우
        if curr.left is None and curr.right is None:
            if direction == "l":
                parent.left = None
            else:
                parent.right = None
        # 하위 노드가 한개 있는 경우
        #   오른쪽

        elif curr.left is None and curr.right is not None:
            if direction == "l":
                parent.left = curr.right
            else:
                parent.right = curr.right
        #   왼쪽

        elif curr.right is None and curr.left is not None:
            if direction == "l":
                parent.left = curr.left
            else:
                parent.right = curr.left

        # 하위 노드가 두 개 모두 있는 경우
        elif curr.right is not None and curr.left is not None:
            if direction == "l":
                parent.left = curr.right
                parent.right = curr.right
                temp = curr.left
                curr = curr.right
                while curr.left is not None:
                    curr = curr.left
                curr.left = temp
            else:
                parent.right = curr.right
                temp = curr.left
                curr = curr.right
                while curr.left is not None:
                    curr = curr.left
                curr.left = temp
        # parent 노드와, 방향을 저장해두어야 함.
        # 오른쪽 하위 노드들을 전부 부모에 갖다붙이고, 삭제하는 왼쪽 노드들을 오른쪽 노드의 최 왼쪽 노드에 갖다 붙임


bst = BinarySearchTree()