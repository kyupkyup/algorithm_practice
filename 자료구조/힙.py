class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx//2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            # 삽인된 인덱스의 값이 부모의 값보다 크면 올라가야지?
            return True
        else:
            return False

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2+ 1

        if left_child_popped_idx >= len(self.heap_array):
            #왼쪽도 없을때
            return False
        elif right_child_popped_idx>= len(self.heap_array):
            # 오른쪽 노드가 없을 때
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                # 왼쪽 노드가 더 클 때, 즉 상위 노드가 정상적이지 않을때
                return True
            else:
                return False
        else:
            # 왼, 오 모두 있을 때
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                # 왼쪽이 크면 왼쪽만 상위 노드랑 비교하면됨
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    #상위 노드가 왼쪽 노드보다 작으면 바꿔야됨
                    return True
                else:
                    return False

            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False


    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx] ,self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True

    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]

        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            #오른쪽만 없을 경우
            if right_child_popped_idx >= len(self.heap_array):
                # 상위 노드의 오른쪽 노드가 없으면
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    # 올라온 노드가 왼쪽 노드 보다 작으면
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
                    # 스왑

            else:
                # 둘 다 있을 경우
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    # 왼쪽 노드가 더 클 경우
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx
        return returned_data

heap = Heap(1)
heap.insert(3)
heap.insert(2)
heap.insert(6)
heap.insert(7)
heap.insert(1)
heap.insert(5)
heap.insert(4)

print(heap.heap_array)

#[None, 7, 6, 5, 4, 3, 1, 2, 1]