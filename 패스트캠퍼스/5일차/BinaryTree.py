import array


class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)


    def preorder(self):
        def preorder_traversal(index):
            if index > len(self.array):
                return False
            else:
                print(index, end=" ")
                preorder_traversal(index * 2)
                preorder_traversal(index * 2 + 1)

        root = 1
        preorder_traversal(root)
        print()

    def inorder(self):
        def inorder_traversal(index):
            if index > len(self.array):
                return False
            else:
                inorder_traversal(index * 2)
                print(index, end=" ")
                inorder_traversal(index * 2 + 1)
        root = 1
        inorder_traversal(root)
        print()

    def postorder(self):
        def postorder_traversal(index):
            if index > len(self.array):
                return False
            else:
                postorder_traversal(index * 2)
                postorder_traversal(index * 2 + 1)
                print(index, end=" ")
        root = 1
        postorder_traversal(root)
        print()

    def bfs(self, value):
        for i in range(len(self.array)):
            if self.array[i] == value:
                print(i)
                return
        print(False)
        return

    def dfs(self, value):
        answer = -1
        def dfs_traversal(index):
            nonlocal answer
            if index >= len(self.array):
                return

            if answer >= 0:
                return

            elif self.array[index-1] == value:
                answer = index-1
                return
            else:
                dfs_traversal(index * 2)
                dfs_traversal(index * 2 + 1)
                return
        root = 1
        dfs_traversal(root)

        if answer == -1:
            print(False)
        else:
            print(answer)

arr = []
for i in range(1, 11):
    arr += [i]
bt = BinaryTree(arr)
bt.preorder()
bt.postorder()
bt.inorder()
bt.bfs(6)
bt.bfs(12)
bt.dfs(4)
bt.dfs(9)
bt.dfs(12)