# class Node:
#     def __init__(self, fucked, height):
#         self.left = None
#         self.right = None
#         self.fucked = fucked
#         self.height = 0
#
# class Tree:
#     def __init__(self):
#         self.root = Node(False)
#         self.height = 0
#
#     def preorder(self, i):
#         def recursive(node):
#
#             if node.left == None:
#                 return
#             else:
#                 recursive(node.left)
#
#             if node.right == None:
#                 return
#             else:
#                 recursive(node.right)
#
#
#         recursive(self.root)
#
#     def search(self):
#         count = 0
#         def recursive(node):
#             nonlocal count
#             if not node.fucked:
#                 count += 1
#
#             if node.left == None:
#                 return
#             else:
#                 recursive(node.left)
#
#             if node.right == None:
#                 return
#             else:
#                 recursive(node.right)
#         recursive(self.root)
#         return count
#
#     def add(self, node):
#         if node.fucked:
#             node.left = None
#             node.right = Node(False)
#         else:
#             node.left = Node(False)
#             node.right = Node(True)
#
# tree = Tree()
# for i in range(4):
#     tree.preorder(i)
# print(tree.search())
# print(tree)
#

N = int(input())
def recur(n):
    if n == 1:
        return 3
    else:
        return recur(n-1) + 2*(n-1)
print(recur(N))

