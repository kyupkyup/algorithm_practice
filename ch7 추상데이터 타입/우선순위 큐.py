# 힙은 각 노드가 하위 노드보다 작은 이진 트리를 뜻함
#
# 트리가 수정될 때, 다시 트리를 구성하는 데 O(logN) 소요

import heapq
list1 = [4, 6, 8, 1]
heapq.heapify(list1)
print(list1)

heapq.heappush(list1, -5)
print(list1)

