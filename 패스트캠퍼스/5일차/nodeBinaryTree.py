from _collections import deque

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]

        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        def recursive(node):
            print(node.value, end=" ")

            if node.left == None:
                return
            else:
                recursive(node.left)

            if node.right == None:
                return
            else:
                recursive(node.right)
        recursive(self.root)
        print()

    def inorder(self):

        def recursive(node):

            if node.left == None:
                print(node.value, end=" ")

                return
            else:
                recursive(node.left)
            print(node.value, end=" ")

            if node.right == None:
                return
            else:
                recursive(node.right)
        recursive(self.root)
        print()

    def postorder(self):
        def recursive(node):
            if node.left == None:
                print(node.value, end=" ")
                return
            else:
                recursive(node.left)

            if node.right == None:
                print(node.value, end=" ")
                return
            else:
                recursive(node.right)
            print(node.value, end=" ")
        recursive(self.root)
        print()

    def bfs(self, value):
        dq = deque([])
        dq.append(self.root)

        while dq:
            num = dq.popleft()
            if num.value == value:
                return True
            else:
                if num.left is not None:
                    dq.append(num.left)
                if num.right is not None:
                    dq.append(num.right)

        return False

    def dfs(self, value):
        answer = False
        def recursive(node):
            nonlocal answer
            if node.value == value:
                answer = True
                return

            if node.left == None:
                return
            else:
                recursive(node.left)

            if node.right == None:
                return
            else:
                recursive(node.right)
        recursive(self.root)
        return answer


        return False


BT = BinaryTree([i for i in range(10)])
BT.preorder()
BT.inorder()
BT.postorder()
print(BT.bfs(2))
print(BT.bfs(12))
print(BT.bfs(2))
print(BT.bfs(12))