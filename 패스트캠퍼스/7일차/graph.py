from _collections import deque


class Vertex:
    def __init__(self, value, adj_list=None):
        self.value = value
        if adj_list is None:
            adj_list = []
        self.adj_list = adj_list


class Graph:
    def __init__(self):
        self.vertices = []

    def insert(self, value, adj_list):
        v = Vertex(value, adj_list)
        self.vertices.append(v)
        for adj_v_ind in v.adj_list:
            if adj_v_ind < len(self.vertices):
                self.vertices[adj_v_ind].adj_list.append(len(self.vertices)-1)

    def bfs(self, vert_ind, value):
        visited = [False for i in range(len(self.vertices))]
        dq = deque([])
        dq.append(vert_ind)
        visited[vert_ind] = True

        while dq:
            index = dq.popleft()
            print(index, end=" ")
            if self.vertices[index].value == value:
                return True
            else:
                for i in range(len(self.vertices[index].adj_list)):
                    if not visited[self.vertices[index].adj_list[i]]:
                        visited[self.vertices[index].adj_list[i]] = True
                        dq.append(self.vertices[index].adj_list[i])

        return False

    def dfs(self, vert_ind, value):
        visited = [False for i in range(len(self.vertices))]
        visited[vert_ind] = True
        ans = False

        def recursive(index):
            nonlocal ans


            print(index, end=" ")
            if self.vertices[index].value == value:
                ans = True
                return



            for adj_v_ind in range(len(self.vertices[index].adj_list)):
                if not visited[self.vertices[index].adj_list[adj_v_ind]]:
                    visited[self.vertices[index].adj_list[adj_v_ind]] = True
                    recursive(self.vertices[index].adj_list[adj_v_ind])
                    if ans:
                        return
            return

        recursive(vert_ind)

        return ans


graph = Graph()
graph.insert(0, [4])
graph.insert(1, [0])
graph.insert(2, [1])
graph.insert(3, [2])
graph.insert(4, [0, 2, 3])
print(graph.bfs(0, 2))
print(graph.dfs(0, 2))
