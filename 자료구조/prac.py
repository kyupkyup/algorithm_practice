# class MinHeap:
#     def __init__(self):
#         self.arr = []
#
#     def insert(self, value):
#         self.arr.append(value)
#         i = len(self.arr) - 1
#
#         while i > 0:
#             j = i // 2
#             if self.arr[i] > self.arr[j]:
#                 break
#             else:
#                 self.arr[i], self.arr[i] = self.arr[j], self.arr[i]
#                 i = j

def solution(x, y):
    ans = []
    a = dict()
    for i in y:
        a[i] = 1
    for j in x:
        if j in a:
            ans.append(True)
        else:
            ans.append(False)
    return ans
print(solution([1,2,3,33,2,2,1,1], [1,2]))