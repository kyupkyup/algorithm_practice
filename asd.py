class Node:
    def __init__(self, value, left=None, right=None):
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
                if curr.value == value:
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

    def print_sorted(self):
        def recursive(node):
            if node is None:
                return
            else:
                recursive(node.left)
                print(node.value)
                recursive(node.right)
        recursive(self.root)
        return

bt = BinarySearchTree()

bt.insert(2)
bt.insert(10)
bt.insert(20)
bt.insert(0.5)
bt.insert(1)
bt.insert(4)
bt.insert(3)
bt.insert(5)
bt.insert(7)
bt.insert(-1)
bt.insert(10)
bt.print_sorted()
