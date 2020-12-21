# 힙은 각 노드가 하위 노드보다 작은 이진 트리를 뜻함
#
# 트리가 수정될 때, 다시 트리를 구성하는 데 O(logN) 소요

import heapq


class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self._index = 0

    def push(self,item, priority):
        heapq.heappush(self.queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({0!r})".format(self.name)


def test_priority_queue():
    q=PriorityQueue()
    q.push(Item("test1"), 1)
    q.push(Item("test2"), 4)
    q.push(Item("test3"), 3)
    q.push(Item("test4"), 2)

    print(str(q.pop()))


if __name__ == "__main__":
    test_priority_queue()
