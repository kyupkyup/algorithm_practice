import array


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.isFull = False
        self.array = array.array('l', [0] * capacity)


    def put(self, value):
        if self.isFull is True:
            return False

        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        # capacity 를 초과할 경우

        if self.rear == self.front:
            self.isFull = True
        return True

        # full 일 경우

    def get(self):
        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity

        if self.rear == self.front and self.isFull is False:
            return False
        self.isFull = False

        return value

    def peek(self):
        if self.array[self.front] == self.array[self.rear] and self.isFull is False:
            return False
        return self.array[self.rear]

    def print(self):
        if self.array[self.front] == self.array[self.rear] and self.isFull is False:
            print([])
            return

        start = self.front
        end = self.rear
        if self.rear <= self.front:
            end += self.capacity

        for i in range(start, end):
            print(self.array[i % self.capacity], end=" ")

        print()


cq = CircularQueue(9)
for i in range(5):
    cq.put(i)
cq.print()
for _ in range(2):
    cq.get()
cq.print()
for i in range(5):
    cq.put(i)
cq.print()