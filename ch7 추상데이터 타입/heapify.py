class MaxHeap(object):
    def __init__(self):
        self.queue = [3, 2, 5, 1, 7, 8, 2]
        for i in range(len(self.queue)//2, -1, -1):
            self.__max_heapify__(i)

    def insert(self, n):
        self.queue.append(n)
        for i in range(len(self.queue)//2, -1, -1):
            self.__max_heapify__(i)

    def delete(self):
        max_element = self.queue[0]
        n = len(self.queue)
        self.queue[0] = self.queue[n-1]
        self.queue = self.queue[:(n-1)]
        self.__max_heapify__(0)
        return max_element

    def __max_heapify__(self, i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)
        current_point_index = i

        if left_index <= len(self.queue) - 1 and self.queue[current_point_index] < self.queue[left_index]:
            # left_index가 전체 길이보다 작은 경우에만, 크면 존재하지 않는 자식 노드에 접근 한 것
            # current_point_index의 값과 left_index의 값을 비교 해서 부모 노드가 더 작은 경우
            current_point_index = left_index
            # 왼쪽으로 포인터를 옮겨줌

        if right_index <= len(self.queue) - 1 and self.queue[current_point_index] < self.queue[right_index]:
            # 만약 오른쪽이랑 비교했는데 오른쪽 노드가  더 크다면 오른쪽 노드를 올려주고
            # 그게 아니면 자동으로 왼쪽 노드가 올라감
            current_point_index = right_index

        if current_point_index != i:
            # 변화가 있었다면, 즉 왼쪽이나 오른쪽 노드와 변화가 있으면
            self.swap(i, current_point_index)  # 더 큰 노드와 현재 부모 노드를 바꿔줌
            self.__max_heapify__(current_point_index)  # 재귀적으로 heapify

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def parent(self, index):
        return (index - 1) // 2

    def leftchild(self, index):
        return index * 2 + 1

    def rightchild(self, index):
        return index * 2 + 2

    def printHeap(self):
        print(self.queue)

if __name__ == "__main__":
    maxHeap = MaxHeap()
    maxHeap.insert(10)
    maxHeap.insert(5)
    maxHeap.delete()


    maxHeap.printHeap()