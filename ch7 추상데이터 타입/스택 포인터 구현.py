
class Node(object):
    def __init(self, value=None, pointer =None):
        self.value = value
        self.pointer = pointer

class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head) # 헤드 업데이트
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print("stack is empty")

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("stack is empty")

    def size(self):
        return self.count

