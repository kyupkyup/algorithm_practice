from _collections import deque

def solution(a, edges):
    def delete(dq):
        for node_idx in dq:
            if arr[arr[node_idx][0]]:
                if node_idx in arr[arr[node_idx][0]]:
                    arr[arr[node_idx][0]].remove(node_idx)


    length_a = len(a)
    arr = [[] for _ in range(length_a)]
    for edge in edges:
        arr[edge[0]].append(edge[1])
        arr[edge[1]].append(edge[0])

    if sum(a) == 0:
        count = 0
        while True:
            dq = deque([])
            for node_idx in range(len(arr)):
                if len(arr[node_idx]) == 1 and a[node_idx] != 0:
                    dq.append(node_idx)
                    if a[node_idx] >= 0:
                        count += a[node_idx]
                        a[arr[node_idx][0]] += a[node_idx]
                        a[node_idx] = 0
                    else:
                        count += abs(a[node_idx])
                        a[arr[node_idx][0]] -= a[node_idx]
                        a[node_idx] = 0
            delete(dq)
            cnt = 0
            for i in a:
                if i == 0:
                    cnt += 1
            if cnt == length_a:
                return count



    else:
        return -1

    return count
a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))
