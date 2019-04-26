# implementation of an undirected graph using Adjacency Matrix, with weighted edges
class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex,):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            return True
        else:
            return False

    # Formatting does not allow for weights over 3 digits in length, negative signs occupies a digit
    def print_graph(self):
        string = ''
        for v in self.vertices:
            string += v + ' | '
        print('  | ' + string + '')
        for v, i in sorted(self.edge_indices.items()):
            print(v, end=' |')
            for j in range(len(self.edges)):
                if len(str(self.edges[i][j])) == 1:
                    print(' ' + str(self.edges[i][j]), end=' |')
                    # print(self.edges[i][j], end=' |')
                elif len(str(self.edges[i][j])) == 2:
                    print(self.edges[i][j], end=' |')
                else:
                    print(self.edges[i][j], end='|')
            print(' ')
