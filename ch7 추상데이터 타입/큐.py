class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item) # 앞에서 들어가기 떄문에 메모리에서 데이터들이 이동 -> 삽입 O(n)

    def dequeue(self):
        if not self.items:
            print("already empty")
        else:
            value = self.items.pop()
            return value

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("empty")

queue = Queue()
queue.enqueue("1")



























































