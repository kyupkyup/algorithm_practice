class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def prepend(self, value):
        if self.head == None:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(value, self.head, None)
            self.head.prev = node
            self.head = node
        self.length += 1

    def append(self, value):
        if self.tail == None:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node
        self.length += 1

    def set_head(self, index):
        if self.length <= index or index < 0:
            return "list index out of range"
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            self.head = curr
            self.head.prev = None
        self.length -= index

    def set_tail(self, index):
        if self.length <= index or index < 0:
            return "list index out of range"
        else:
            curr = self.tail
            for _ in range(self.length - index):
                curr = curr.prev
            self.tail = curr
            self.tail.next = None
        self.length -= (self.length - index)


    def access(self, index):
        if self.length <= index or index < 0:
            return "list index out of range"
        else:
            if index >= self.length // 2:
                # 인덱스가 절반보다 클 경우 tail에서부터 접근
                curr = self.tail
                for _ in range(self.length - index - 1):
                    curr = curr.prev
                return curr.value

            else:
                # 반대일 경우 head에서부터 접근
                curr = self.head
                for _ in range(index):
                    curr = curr.next
                return curr.value

    def insert(self, index, value):
        if self.length <= index or index < 0:
            return "list index out of range"
        else:
            if index == 0:
                self.prepend(value)
            elif index == self.length-1:
                self.appe0nd(value)
            else:
                if index >= self.length // 2:
                    # 인덱스가 절반보다 클 경우 tail에서부터 접근
                    curr = self.tail
                    for _ in range(self.length - index):
                        curr = curr.prev
                    node = Node(value, curr.next, curr)
                    curr.next = node

                else:
                    # 반대일 경우 head에서부터 접근
                    curr = self.head
                    for _ in range(index-1):
                        curr = curr.next
                    node = Node(value, curr.next, curr)
                    curr.next = node
                self.length += 1

    def remove(self, index):
        if self.length <= index or index < 0:
            return "list index out of range"
        else:
            if index >= self.length // 2:
                # 인덱스가 절반보다 클 경우 tail에서부터 접근

                if index == self.length -1:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    curr = self.tail
                    for _ in range(self.length - index):
                        curr = curr.prev
                    curr.next = curr.next.next
                    curr.next.prev = curr

            else:
                # 반대일 경우 head에서부터 접근
                if index == 0:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    curr = self.head
                    for _ in range(index - 1):
                        curr = curr.next
                    curr.next = curr.next.next
                    curr.next.prev = curr
            self.length -= 1

    def print(self):
        curr = self.head
        while curr != None:
            print(curr.value, end=" ")
            curr = curr.next
        print()

    def print_inverse(self):
        curr = self.tail
        while curr != None:
            print(curr.value, end=" ")
            curr = curr.prev
        print()

