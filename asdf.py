

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    # def __init__(self, root):
    #     self.root = root
    #
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

    def bfs(self, target):
        queue = list()
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            if node.value == target:
                return True
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return False

bt = BinaryTree([1,2,3,4,5,6,7,8])
print(bt.bfs(4))

