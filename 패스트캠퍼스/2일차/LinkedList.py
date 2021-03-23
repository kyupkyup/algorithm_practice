class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def prepend(self, value):
        if self.head == None:
            node = Node(value, None)
        else:
            node = Node(value, self.head)
        self.head = node
        self.length += 1

    def append(self, value):
        if self.head == None:
            node = Node(value, None)
            self.head = node
        else:
            node = Node(value, None)
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node
        self.length += 1

    def set_head(self, index):
        if self.length <= index or index < 0:
            return "list index out of range"
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            self.head = curr
        self.length -= index


    def access(self, index):
        if self.length <= index or index < 0:
            return "list index out of range"
        else:
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
            else:
                curr = self.head
                for _ in range(index - 1):
                    curr = curr.next
                node = Node(value, curr.next)
                curr.next = node

    def remove(self, index):
        if self.length <= index or index < 0:
            return "list index out of range"
        if index == 0:
            self.head = self.head.next

        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next


    def print(self):
        curr = self.head
        while curr != None:
            print(curr.value, end=" ")
            curr = curr.next
        print()


singlyLinkedList = SinglyLinkedList()
singlyLinkedList.prepend(1)
singlyLinkedList.append(3)
singlyLinkedList.append(4)
singlyLinkedList.append(5)
singlyLinkedList.prepend(10)
singlyLinkedList.print()
print(singlyLinkedList.is_empty())
print(singlyLinkedList.access(2))
singlyLinkedList.insert(1, 10)
singlyLinkedList.print()
singlyLinkedList.remove(2)
singlyLinkedList.print()
singlyLinkedList.set_head(2)
singlyLinkedList.print()
