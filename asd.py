class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, data):
        curr = self.root
        for c in data:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]

        if "*" not in  curr.children:
            curr.children["*"] = Node("*")



    def get_all_words(self):

        def recursive(node, ans):
            if node.value == "*":
                print(ans)
                return
            ans += node.value
            for i in node.children:
                recursive(node.children[i], ans)
        recursive(self.root, "")
        return

tree = Trie()
tree.insert("abaaa")
tree.insert("abccc")
tree.insert("abccd")
tree.insert("caa")
tree.insert("cca")
print(tree.get_all_words())
#
#
# def search(self):
#     current_node = self.head
#
#     for char in string:
#         if char in current_node.children:
#             current_node = current_node.children[char]
#         else:
#             return False
#
#     if current_node.data:
#         return current_node.data
