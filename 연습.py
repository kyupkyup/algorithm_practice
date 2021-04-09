class MinHeap:
    def __init__(self):
        self.arr = [None]

    def push(self, val):
        self.arr.append(val)
        curr = len(self.arr) - 1

        while curr > 1:
            parent = curr // 2
            if self.need_swap(curr, parent):
                self.swap(curr, parent)
                curr = parent
            else:
                break
    def need_swap(self, curr, parent):
        if self.arr[curr] < self.arr[parent]:
            return True
        else:
            return False

    def swap(self, curr, parent):
        self.arr[curr], self.arr[parent] = self.arr[parent], self.arr[curr]

    def push(self, val):
        self.arr.append(val)
        curr = len(self.arr) - 1

        def recursive(curr):
            if curr <= 1:
                return
            parent = curr // 2

            if self.need_swap(curr, parent):
                self.swap(curr, parent)
                recursive(parent)
            else:
                return
        recursive(curr)
        return

heap = MinHeap()
heap2 = MinHeap()
heap.push(1)
heap.push(4)
heap.push(3)
heap.push(2)
heap2.push_recursive(1)
heap2.push_recursive(4)
heap2.push_recursive(3)
heap2.push_recursive(2)
print()
