class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, comp=None):
        self.root = None
        self.comp = comp

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        parent = None
        direction = None

        while current is not None:
            parent = current
            if self.comp is None:
                if value <current.value:
                    direction="left"
                    current = current.left
                else:
                    direction = "rigth"
                    current = current.right
            else:
                if self.comp(value, current.value) < 0:
                    direction="left"
                    current = current.left
                else:
                    direction = "rigth"
                    current = current.right
        if direction == "left":
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while current is not None:
            parent = current
            if self.comp is None:
                if value == current.value:
                    return True
                elif value < current.value:
                    current = current.left
                else:
                    current = current.right
            else:
                comp = self.comp(value,current.value)
                if comp == 0:
                    return True
                if comp < 0:
                    current = current.left
                else:
                    current = current.right
        return False

def comp_func(s1, s2):
    if s1[0] < s2[0]:
        return -1
    elif s1[0] == s2[0]:
        return 0
    else:
        return 1

bst = BinarySearchTree(comp_func)
items = ["apple", "banana", "delta", "game"]

for item in items:
    bst.insert(item)

queries = ["a", "b", "c","d","e","f","g"]
for query in queries:
    print(query, bst.search(query))

# a true
# b true
# c false
# d true
# e false
# f false
# g true