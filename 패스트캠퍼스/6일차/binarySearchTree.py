class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            curr = self.root
            while curr is not None:
                if value == curr.value:
                    print("already there is node")
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

    def search(self, value):
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return curr
            if value > curr.value:
                curr = curr.right
            else:
                curr = curr.left
        return False

    def remove(self, value):
        parent = None
        direction = "l"
        isHere = False
        curr = self.root
        while curr is not None:
            if value == curr.value:
                isHere = True
                break
            parent = curr
            if value > curr.value:
                direction = "r"
                curr = curr.right
            else:
                direction = "l"
                curr = curr.left

        if not isHere:
            return False

        # 하위 노드가 없는 경우
        if curr.left is None and curr.right is None:
            if direction == "l":
                parent.left = None
            else:
                parent.right = None
        # 하위 노드가 한개 있는 경우
        #   오른쪽

        elif curr.left is None and curr.right is not None:
            if direction == "l":
                parent.left = curr.right
            else:
                parent.right = curr.right
        #   왼쪽

        elif curr.right is None and curr.left is not None:
            if direction == "l":
                parent.left = curr.left
            else:
                parent.right = curr.left

        # 하위 노드가 두 개 모두 있는 경우
        elif curr.right is not None and curr.left is not None:
            if direction == "l":
                parent.left = curr.right
                temp = curr.left
                curr = curr.right
                while curr.left is not None:
                    curr = curr.left
                curr.left = temp
            else:
                parent.right = curr.right
                temp = curr.left
                curr = curr.right
                while curr.left is not None:
                    curr = curr.left
                curr.left = temp
        # parent 노드와, 방향을 저장해두어야 함.
        # 오른쪽 하위 노드들을 전부 부모에 갖다붙이고, 삭제하는 왼쪽 노드들을 오른쪽 노드의 최 왼쪽 노드에 갖다 붙임


bst = BinarySearchTree()

import random
x = list(range(20))
random.shuffle(x)
for el in x:
    bst.insert(el)
bst.root.display()

bst.remove(6)
bst.root.display()

bst.remove(10)
bst.root.display()