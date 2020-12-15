
class Stack(object):
    stack_in = []
    stack_out = []

    # 입력할 땐 stack_in 으로 나올때 out 에 넣어서

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_in:
            print("it is empty")
        else:
            if self.stack_out:
                self.stack_out = []

            for i in range(1, len(self.stack_in)+1):
                self.stack_out.append(self.stack_in[-i])
            tmp = self.stack_out.pop()
            self.stack_in = []
            for i in range(1, len(self.stack_out)+1):
                self.stack_in.append(self.stack_out[-i])
            return tmp

    def show_list(self):
        return self.stack_in

    def index(self, idx):
        if len(self.stack_in) < idx:
            print("index overflow the list size")

        else:
            return self.stack_in[idx]
def test():
    stack = Stack()
    stack.enqueue(1)
    stack.enqueue(2)
    stack.enqueue(3)
    stack.enqueue(4)
    print(stack.show_list())
    print(stack.dequeue())
    print(stack.dequeue())

    print(stack.stack_in)
    print(stack.stack_out)
    print(stack.show_list())
    print(stack.dequeue())
    stack.enqueue(5)
    print(stack.dequeue())
    print(stack.show_list())
    stack.enqueue(10)
    stack.enqueue(11)
    print(stack.index(1))
    print(stack.show_list())
test()
