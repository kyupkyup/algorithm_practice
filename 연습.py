

class BinaryTree:
    def __init__(self, array):
        self.array = [None] + array

    def preorder(self):
        def recursive(index):
            if index >= len(self.array):
                return
            print(self.array[index])
            recursive(index * 2)
            recursive(index * 2 + 1)
        recursive(1)

bt = BinaryTree([1,2,3,4,5,6,7,8,9])
bt.preorder()








