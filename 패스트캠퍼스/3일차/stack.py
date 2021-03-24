import array


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0] * capacity)

    def push(self, value):
        if self.top == self.capacity:
            print("stack overflow")
            return False
        else:
            self.array[self.top] = value
            self.top += 1

    def pop(self):
        if self.top == 0:
            print("stack underflow")
            return False
        else:
            self.top -= 1
            pop_value = self.array[self.top]
            return pop_value

    def peek(self):
        if self.top == 0:
            return "nothing to see"
        else:
            return self.array[self.top - 1]

    def is_empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def print(self):
        for i in range(self.top):
            print(self.array[i], end=" ")
        print()


stack = Stack(5)
for i in range(5):
    stack.push(i)
print(stack.peek())
stack.push(10)
stack.print()
stack.pop()
stack.print()
stack.pop()
stack.print()
stack.pop()
stack.print()
stack.pop()
stack.print()
stack.pop()
stack.pop()
stack.pop()
stack.push(10)
stack.print()
