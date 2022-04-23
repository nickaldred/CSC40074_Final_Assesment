
class Graph():
    """
    Holds all the methods to create and tranverse the city graph.

    """
    def __init__ (self) -> None:
        self.graph = {}
        self.vertices_no = 0

    # Add a vertex to the dictionary
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
        Creates an edge between the given vertex's v1 and v2
        v1 = int or str - 1st vertex
        v2 = int or str - 2nd vertex
        e = int -  edge weight
        """

        # Check if vertex v1 is valid
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is valid 
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
        Prints the adjacency list dictionary in an adjacency list format.

        """

        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")


    def print_city_list(self) -> None:
        """
        Prints a list of the vertices (city's) that exist in the graph.

        """

        print("\nList of citys:")
        for vertex in self.graph:
            print(f"City: {vertex}")


    def search_vertex(self, key) -> bool:
        """
        Searchs the graph with a given key to see a matching vertex exists.

        """
        for vertex in self.graph:
            if vertex == key:
                return(True)
        return(False)


    def create_city_graph(self) -> None:
        """
        Creates a adjacency list graph using the data from the assessment brief.

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
        # corresponding weights
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


    def bfs(self, node, key):
        """
        Performs a breadth-first search on the stored city graph using
        a provided starting node and search key.

        input:
        node - int or str - Starting node for search.
        key - int or str - Node to searched for

        """
        visited = [] # List to keep track of visited nodes.
        queue = []     #Initialize a queue
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 

            for neighbour in self.graph[s[0]]:
                if neighbour not in visited:
                    if neighbour[0] == key:
                        return(True)
                    visited.append(neighbour)
                    queue.append(neighbour)
        return(False)




    def dfs(self, node, key, visited):
        """
        Performs a depth-first search on the stored city graph using
        a provided starting node and search key.

        input:
        node - int or str - Starting node for search.
        key - int or str - Node to searched for
        visited - empty list - Empty list to store visted nodes.

        """
        if key in visited:
            return(True)
        if node not in visited:

            visited.add(node)
            for neighbour in self.graph[node]:

                self.dfs(neighbour[0], key, visited)
                if key in visited:
                    return(True)
        
        return(False)







#graph.print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
#print ("Internal representation: ", graph.graph)

graph = Graph()

graph.create_city_graph()

#print(graph.search_vertex('A'))
graph.print_formatted_graph()

#print(graph.bfs("A", "a"))

# visited = set() # Set to keep track of visited nodes.
# print(graph.dfs("K", "A", visited, False))

#graph.print_city_list()