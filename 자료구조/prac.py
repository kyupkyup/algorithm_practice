import heapq

a=[4,5,1,8,7,6,10]
print(len(a))
heapq.heapify(a)
print(len(a))

while a:
    print(heapq.heappop(a))

#[1, 5, 4, 8, 6, 7, 10]
#[1, 5, 4, 8, 7, 6, 10]