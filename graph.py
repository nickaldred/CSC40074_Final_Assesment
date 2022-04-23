
class Graph():
    def __init__ (self):
        self.graph = {}
        self.vertices_no = 0

    # Add a vertex to the dictionary
    def add_vertex(self, v):
        if v in self.graph:
            print("Vertex ", v, " already exists.")
        else:
            self.vertices_no = self.vertices_no + 1
            self.graph[v] = []

    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e):

        # Check if vertex v1 is a valid vertex
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            # Since this code is not restricted to a directed or 
            # an undirected graph, an edge between v1 v2 does not
            # imply that an edge exists between v2 and v1
            temp = [v2, e]
            self.graph[v1].append(temp)

            temp = [v1, e]
            self.graph[v2].append(temp)

    # Print the graph
    def print_graph(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

    def print_formatted_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
# driver code

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_vertex('G')
graph.add_vertex('H')
graph.add_vertex('I')
graph.add_vertex('J')
graph.add_vertex('K')
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
graph.add_edge('A', 'C', 15)
graph.add_edge('A', 'G', 11)
graph.add_edge('A', 'B', 2)
graph.add_edge('B', 'F', 6)
graph.add_edge('F', 'H', 1)
graph.add_edge('F', 'E', 5)
graph.add_edge('C', 'D', 18)
graph.add_edge('B', 'D', 5)
graph.add_edge('G', 'H', 3)
graph.add_edge('D', 'E', 6)
graph.add_edge('D', 'K', 11)
graph.add_edge('E', 'K', 12)
graph.add_edge('E', 'I', 13)
graph.add_edge('I', 'J', 5)
graph.add_edge('K', 'J', 37)
#graph.print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
#print ("Internal representation: ", graph.graph)

graph.print_formatted_graph()
