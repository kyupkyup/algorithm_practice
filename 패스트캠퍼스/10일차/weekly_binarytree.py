class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return

        curr = self.root
        while True:
            if value > curr.value:
                if curr.right is None:
                    curr.right = Node(value)
                    return
                curr = curr.right

            else:
                if curr.left is None:
                    curr.left = Node(value)
                    return
                curr = curr.left

    def search(self, value):
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return True
            if value > curr.value:
                curr = curr.right
            else:
                curr = curr.left


    def remove(self, value):
        curr = self.root
        parent = None
        direction = "l"
        isHere = False
        while curr is not None:
            if value == curr.value:
                isHere = True
                break
            if value > curr.value:
                parent = curr
                direction = "r"
                curr = curr.right
            else:
                parent = curr
                direction = "l"
                curr = curr.left
        if not isHere:
            return False

        if curr.left is None and curr.right is None:
            if direction == "l":
                parent.left = None
            else:
                parent.right = None

        elif curr.left is None and curr.right is not None:
            if direction == "l":
                parent.left = curr.right
            else:
                parent.right = curr.right
        elif curr.left is not None and curr.right is None:
            if direction == "l":
                parent.left = curr.left
            else:
                parent.right = curr.left
        elif curr.left is not None and curr.right is not None:
            if direction == "l":
                temp = curr.left
                parent.left = curr.right
                while curr.left is not None:
                    curr = curr.left
                curr.left = temp
            else:
                temp = curr.left
                parent.right = curr.right
                while curr.left is not None:
                    curr = curr.left
                curr.left = temp