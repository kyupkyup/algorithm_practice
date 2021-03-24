import array

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):

        if self.rear >= self.capacity:
            print("queue index out")
            return

        self.array[self.rear] = value
        self.rear += 1

    def get(self):
        if self.front == self.rear:
            print("queue is empty")
            return

        value = self.array[self.front]
        self.front += 1

        return value

    def peek(self):
        if self.front == self.rear:
            print("queue is empty")
            return
        return self.array[self.front]

    def print(self):
        for i in range(self.front, self.rear):
            print(self.array[i], end=" ")
        print()
lq = LinearQueue(3)
for i in range(3):
    lq.put(i)
lq.print()
lq.put(4)
lq.print()
lq.get()
lq.print()