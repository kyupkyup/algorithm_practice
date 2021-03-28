class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class CircularList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            node = Node(value, None)
            node.next = node
            self.head = node

        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            node = Node(value, self.head)
            curr.next = node


    def print(self):
        curr = self.head
        while curr.next != self.head:
            print(curr.value)
            curr = curr.next


cL = CircularList()
cL.append(4)
cL.append(3)
cL.append(2)
cL.append(1)
cL.print()