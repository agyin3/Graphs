"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # q = Queue()
        q = Queue()

        # visited = {}
        visited = set()

        ## vertices = self.vertices
        vertices = self.vertices

        # q.enqueue(starting_vertex)
        q.enqueue(starting_vertex)

        # while q.empty() is False:
        while q.size() > 0:
            #### item = q.get()
            item = q.dequeue()
            # visited.add(item)
            visited.add(item)
            print(item)
            # for v in vertices[item]:
            for v in vertices[item]:
                # if v not in visited:
                if v not in visited:
                    # q.enqueue(v)
                    q.enqueue(v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # s = Stack()
        s = Stack()

        # visited = set()
        visited = set()

        # vertices = self.vertices
        vertices = self.vertices

        # s.push(starting_vertex)
        s.push(starting_vertex)

        # while s.size() > 0:
        while s.size() > 0:
            # print(f's: {s.stack}')
            ## item = s.pop()
            item = s.pop()
            # if item in visited:
            if item in visited:
                # continue
                continue
            # visited.add(item)
            visited.add(item)
            print(item)
            # for v in vertices[item]:
            for v in vertices[item]:
                # s.push(v)
                s.push(v)

    def dft_recursive(self, starting_vertex, visited=set(), stack=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # FIRST ITERATION
        ## s = set() if stack is None else stack
        s = Stack() if stack is None else stack

        # BASE CASE
        # if starting_vertex in visited:
        if starting_vertex in visited:
            # return
            return

        # Normal Case
        ## vertices = self.vertices
        vertices = self.vertices
        # visited.add(item)
        visited.add(starting_vertex)
        # print(item)
        print(starting_vertex)
        # for v in vertices[item]:
        for v in vertices[starting_vertex]:
            # s.push(v)
            s.push(v)
        ## next_vertex = s.pop()
        next_vertex = s.pop()
        # if next_vertex is None:
        if next_vertex is None:
            # return
            return
        # return self.dft_recursive(next_vertex, visited, s)
        return self.dft_recursive(next_vertex, visited, s)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # q = Queue()
        q = Queue()

        # visited = {}
        visited = set()
        path = []

        ## vertices = self.vertices
        vertices = self.vertices

        # q.enqueue(starting_vertex)
        q.enqueue(starting_vertex)

        # while q.empty() is False:
        while q.size() > 0:
            #### item = q.get()
            item = q.dequeue()
            # visited.add(item)
            visited.add(item)
            path.append(item)

            # if item = destination_vertex:
            if item == destination_vertex:
                # return path
                return path
            # for v in vertices[item]:
            for v in vertices[item]:
                # if v not in visited:
                if v not in visited:
                    # q.enqueue(v)
                    neighbors = self.get_neighbors(v)

                    if destination_vertex in neighbors:
                        path.append(v)
                        path.append(destination_vertex)
                        return path

                    q.enqueue(v)

        return False

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # s = Stack()
        s = Stack()

        # visited = set()
        visited = set()

        # vertices = self.vertices
        vertices = self.vertices
        path = []

        # s.push(starting_vertex)
        s.push(starting_vertex)

        # while s.size() > 0:
        while s.size() > 0:
            # print(f's: {s.stack}')
            ## item = s.pop()
            item = s.pop()
            # if item in visited:
            if item in visited:
                # continue
                continue
            # visited.add(item)
            visited.add(item)
            path.append(item)

            if item == destination_vertex:
                return path
            # for v in vertices[item]:
            for v in vertices[item]:
                # if v not in visited:
                if v not in visited:
                    # q.enqueue(v)
                    neighbors = self.get_neighbors(v)

                    if destination_vertex in neighbors:
                        path.append(v)
                        path.append(destination_vertex)
                        return path
                # s.push(v)
                s.push(v)

        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), stack=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # FIRST ITERATION
        ## s = set() if stack is None else stack
        s = Stack() if stack is None else stack

        # BASE CASE
        # if starting_vertex in visited:
        if starting_vertex in visited:
            # return
            return

        # Normal Case
        ## vertices = self.vertices
        vertices = self.vertices
        # visited.add(item)
        visited.add(starting_vertex)
        # print(item)
        path.append(starting_vertex)
        # for v in vertices[item]:
        for v in vertices[starting_vertex]:
            neighbors = self.get_neighbors(v)
            if destination_vertex in neighbors:
                path.append(v)
                path.append(destination_vertex)
                return path
            # s.push(v)
            s.push(v)
        ## next_vertex = s.pop()
        next_vertex = s.pop()
        # if next_vertex is None:
        if next_vertex is None:
            # return
            return
        # return self.dft_recursive(next_vertex, visited, s)
        return self.dfs_recursive(next_vertex, destination_vertex, visited, s, path)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
