
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self, ):
        if self.items is not None:
            return self.items.pop()
        else:
            print("stack is empty, you cannot pop")

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return not bool(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        