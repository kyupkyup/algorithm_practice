class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newData):
        self.value = newData

    def setNext(self, newPointer):
        self.pointer = newPointer


class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def printList(self):
        node = self.head
        while node:
            print(node.value, end="")
            node = node.pointer

    def delete(self):
        self.length -= 1
        node = self.head
        self.head = node.pointer

    def add(self, value):
        self.length += 1
        self.head = Node(value, self.head)

if __name__ =="__main__":
    ll = LinkedListLIFO()
    for i in range(1, 5):
        ll.add(i)
    ll.delete()
    ll.add(5)
    ll.printList()