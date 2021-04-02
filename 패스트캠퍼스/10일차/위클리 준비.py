import array


class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)

    def preorder(self):
        def recursive(index):
            if index >= len(self.array):
                return
            print(self.array[index], end=" ")
            recursive(index * 2 + 1)
            recursive(index * 2 + 2)

        recursive(0)
        print()

    def inorder(self):
        def recursive(index):
            if index >= len(self.array):
                return
            recursive(index * 2 + 1)
            print(self.array[index], end=" ")
            recursive(index * 2 + 2)

        recursive(0)
        print()
    def postorder(self):
        def recursive(index):
            if index >= len(self.array):
                return
            recursive(index * 2 + 1)

            recursive(index * 2 + 2)
            print(self.array[index], end=" ")

        recursive(0)
        print()
    def bfs(self, value):
        return False

    def dfs(self, value):
        return False


bt = BinaryTree([1, 5, 4, 3, 6, 7, 8, 9, 1, 123, 10])
bt.preorder()
bt.inorder()
bt.postorder()


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeNode:
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
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass

    def bfs(self, value):
        return False

    def dfs(self, value):
        return False
