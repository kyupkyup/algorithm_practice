from DoubleLinkedList import DoublyLinkedList

class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue(DoublyLinkedList):
    def __init__(self):
        DoublyLinkedList.__init__(self)
        self.head = None
        self.tail = None

    def put(self, value):
        super().append(value)

    def get(self):
        value = super().access(0)
        super().remove(0)
        return value

    def peek(self):
        return super().access(0)

    def print(self):
        super().print()

linq = LinkedQueue()
linq.put(3)
linq.print()
linq.put(4)
linq.print()
linq.put(5)
linq.print()
linq.get()
print(linq.peek())
linq.print()