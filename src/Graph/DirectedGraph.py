import collections


class Vertex:

    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = {}

    def addNeighors(self, vertex_id, weight):
        if vertex_id not in self.neighbors:
            self.neighbors[vertex_id] = weight
        else:
            self.neighbors[vertex_id] = weight

    def __repr__(self):
        return f"Vertex id {self.id} with neighbors {self.neighbors}"

class DirectedGraph:

    def __init__(self):
        self.vertexes = {}

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.id not in self.vertexes:
            self.vertexes[vertex.id] = vertex
            return True
        else:
            return False

    def addEdge(self, v1, v2, weight):
        if v1 in self.vertexes and v2 in self.vertexes:
            self.vertexes[v1].addNeighors(v2, weight)
            # self.vertexes[v2].addNeighors(v1, weight) Creating edge only from v1 to v2
            # print(f"Added Edge from {v1} to {v2}")
        # else:
            # print(f"Graph missing vertex {v1} or {v2}")

    def __repr__(self):
        print("------------------------")
        print("Printing Graph")
        for ind, vertex in self.vertexes.items():
            print(f"Vertex {vertex}")
        print('Printing complete')
        print("------------------------")
        return ''

    def bfs(self, start_id):
        visited = set()
        visited.add(start_id)
        que = collections.deque()
        que.append(start_id)
        total_weight = 0
        bfs = []
        while que:
            level_size = len(que)
            for i in range(level_size):
                top = que.popleft()
                bfs.append(str(top))
                edges = self.vertexes[top].neighbors
                for edge, weight in edges.items():
                    if edge not in visited:
                        visited.add(edge)
                        total_weight += weight
                        que.append(edge)

        print (f"Bfs on the graph with starting vertex {start_id} with weight {total_weight} is - ", ' '.join(bfs))


    def dfs(self, start_id):
        visited = set()
        visited.add(start_id)
        stack = []
        stack.append(start_id)
        total_weight = 0
        dfs = []
        while stack:
            top = stack.pop()
            dfs.append(str(top))
            edges = self.vertexes[top].neighbors
            for edge, weight in edges.items():
                if edge not in visited:
                    visited.add(edge)
                    total_weight += weight
                    stack.append(edge)

        print (f"DFS on the graph with starting vertex {start_id} with weight {total_weight} is - ", ' '.join(dfs))

    # Kahn's algorithm
    def topological_sort(self):
        topo_sort = []

        indegree = [0] * (len(self.vertexes))

        for id, vertex in self.vertexes.items():
            for edge in vertex.neighbors.keys():
                indegree[edge - 1] += 1
        stack = []
        for i in indegree:
            if i == 0:
                stack.append(i+1)

        while stack:
            top = stack.pop()
            topo_sort.append(top)
            for edge in self.vertexes[top].neighbors:
                indegree[edge-1] -= 1
                if indegree[edge-1] == 0:
                    stack.append(edge)


        print (topo_sort)




if __name__ == '__main__':
    graph = DirectedGraph()
    for i in range(1, 6):
        graph.addVertex(Vertex(i))

    graph.addEdge(1,3, 4)
    graph.addEdge(3,2, 2)
    graph.addEdge(1,5, 1)
    graph.addEdge(2,5, 5)
    graph.addEdge(3,4, 2)
    graph.addEdge(5,4, 2)

    print(graph)
    # for i in range(1, 6):
    #     graph.dfs(i)
    #     graph.bfs(i)
    graph.topological_sort()


