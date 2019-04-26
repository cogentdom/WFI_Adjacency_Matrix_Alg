# Uses Adj_Matrix to represent and handle the graph
import Adj_Matrix as AdjM
# Graph specific variables
edges = ['AC', 3, 'BA', -4, 'BC', 2, 'CB', -1, 'CD', 7, 'CE', 5, 'DB', 1, 'DE', 10, 'ED', -8]
startVertex = 'A'
endVertex = 'E'

endVertex = chr(ord(endVertex) + 1)
vert = ord(endVertex) - ord(startVertex)
graph = AdjM.Graph()
# Creates vertices
for i in range(ord(startVertex), ord(endVertex)):
    graph.add_vertex(AdjM.Vertex(chr(i)))
# Makes all impossible paths infinite
for i in range(ord(startVertex), ord(endVertex)):
    for j in range(ord(startVertex), ord(endVertex)):
        if i != j:
            graph.add_edge(chr(i), chr(j), float("inf"))
# Creates edges and weights from edges array
for i in range(0, len(edges), 2):
    graph.add_edge(edges[i][:1], edges[i][1:], edges[i + 1])
# Core of Floyd-Warshall Algorithm
for k in range(0, vert):
    print('Table D' + str(k) + ':')
    graph.print_graph()
    print('')
    for i in range(0, vert):
        for j in range(0, vert):
            if graph.edges[i][j] > graph.edges[i][k] + graph.edges[k][j]:
                graph.edges[i][j] = graph.edges[i][k] + graph.edges[k][j]
print('Table D' + str(vert) + ':')
graph.print_graph()
