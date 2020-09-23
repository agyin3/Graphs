from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_vertex):
    graph = Graph()
    for an in ancestors:
        graph.add_vertex(an[0])
        graph.add_vertex(an[1])

        graph.add_edge(an[1], an[0])

    q = Queue()

    visited = set()

    q.enqueue(starting_vertex)

    end_vertices = []

    while q.size() > 0:
        end_vertices = []
        item = q.dequeue()
        visited.add(item)

        neighbors = graph.get_neighbors(item)

        for n in neighbors:
            neighbors_neighbors = graph.get_neighbors(n)

            if not neighbors_neighbors:
                end_vertices.append(n)

            else:
                if n not in visited:
                    q.enqueue(n)

    if len(end_vertices) > 0:
        end_vertices.sort()
        return end_vertices[0]

    else:
        return -1


# def bft(self, starting_vertex):
#     """
#     Print each vertex in breadth-first order
#     beginning from starting_vertex.
#     """
#     # q = Queue()
#     q = Queue()

#     # visited = {}
#     visited = set()

#     ## vertices = self.vertices
#     vertices = self.vertices

#     # q.enqueue(starting_vertex)
#     q.enqueue(starting_vertex)

#     # while q.empty() is False:
#     while q.size() > 0:
#         #### item = q.get()
#         item = q.dequeue()
#         # visited.add(item)
#         visited.add(item)
#         print(item)
#         # for v in vertices[item]:
#         for v in vertices[item]:
#             # if v not in visited:
#             if v not in visited:
#                 # q.enqueue(v)
#                 q.enqueue(v)
