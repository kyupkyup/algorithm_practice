class MinHeap:
    def __init__(self):
        self.arr = []

    def push(self, val):
        index = len(self.arr) - 1
        self.arr.append(val)

        while (index - 1) // 2 >= 0:
            if self.arr[(index - 1) // 2] > self.arr[index]:
                self.arr[(index - 1) // 2], self.arr[index] = self.arr[index], self.arr[(index - 1) // 2]
                index = (index - 1) // 2
            else:
                break

    def pop(self):
        if not self.is_empty():
            return False

        ans = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()

        index = 0
        length = len(self.arr)
        while index * 2 + 2 < len(self.arr):
            left = index * 2 + 1
            right = index * 2 + 2
            if left < length and right < length:
                if self.arr[index] <= self.arr[left] and self.arr[index] <= self.arr[right]:
                    break

                elif self.arr[index] > self.arr[left] and self.arr[index] <= self.arr[right]:
                    self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
                    index = left

                elif self.arr[index] <= self.arr[left] and self.arr[index] > self.arr[right]:
                    self.arr[index], self.arr[right] = self.arr[right], self.arr[index]
                    index = right

                elif self.arr[index] > self.arr[left] and self.arr[index] > self.arr[right]:
                    if self.arr[left] > self.arr[right]:
                        self.arr[index], self.arr[right] = self.arr[right], self.arr[index]
                        index = right
                    else:
                        self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
                        index = left

        return ans

    def peek(self):
        if not self.is_empty():
            print(self.arr[0])
        else:
            print("no value")

    def is_empty(self):
        if not self.arr:
            return False
        else:
            return True


heap = MinHeap()
heap.push(5)
heap.push(1)
heap.push(3)
heap.push(10)
heap.push(2)
heap.push(7)
heap.push(1)
heap.push(2)
heap.push(3)
heap.push(12)
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())

print(heap.pop())
print(heap.pop())
print(heap.pop())
