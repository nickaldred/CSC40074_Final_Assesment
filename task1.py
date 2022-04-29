
class Graph():
    """
    Holds all the methods to create and tranverse the city graph.

    """
    def __init__ (self) -> None:
        self.graph = {}
        self.vertices_no = 0

    # Add a vertex to the dictionary.
    def add_vertex(self, v) -> None:
        """
        Adds a vertex to the adjacency list dictionary.

        Input:
        v = int or str 
        """

        if v in self.graph:
            print("Vertex ", v, " already exists.")
        else:
            self.vertices_no = self.vertices_no + 1
            self.graph[v] = []

    
    def add_edge(self, v1, v2, e) -> None:
        """
        Creates an edge between the given vertex's v1 and v2.
        v1 = int or str - 1st vertex
        v2 = int or str - 2nd vertex
        e = int -  edge weight
        """

        # Check if vertex v1 is valid.
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is valid. 
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            # Adds edges going both ways as graph is undirected.
            temp = [v2, e]
            self.graph[v1].append(temp)

            temp = [v1, e]
            self.graph[v2].append(temp)


    def print_formatted_graph(self) -> None:
        """
        Prints the adjacency list dictionary in an adjacency list 
        format.

        """

        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")


    def create_city_graph(self) -> None:
        """
        Creates a adjacency list graph using the data from the 
        assessment brief.

        """

        #Add's the vertex's to the adjacency list.
        self.add_vertex('A')
        self.add_vertex('B')
        self.add_vertex('C')
        self.add_vertex('D')
        self.add_vertex('E')
        self.add_vertex('F')
        self.add_vertex('G')
        self.add_vertex('H')
        self.add_vertex('I')
        self.add_vertex('J')
        self.add_vertex('K')

        # Add the edges of the graph to the adjacency list with their 
        # corresponding weights.
        self.add_edge('A', 'C', 15)
        self.add_edge('A', 'G', 11)
        self.add_edge('A', 'B', 2)
        self.add_edge('B', 'F', 6)
        self.add_edge('F', 'H', 1)
        self.add_edge('F', 'E', 5)
        self.add_edge('C', 'D', 18)
        self.add_edge('B', 'D', 5)
        self.add_edge('G', 'H', 3)
        self.add_edge('D', 'E', 6)
        self.add_edge('D', 'K', 11)
        self.add_edge('E', 'K', 12)
        self.add_edge('E', 'I', 13)
        self.add_edge('I', 'J', 5)
        self.add_edge('K', 'J', 37)



graph = Graph()

graph.create_city_graph()

graph.print_formatted_graph()
