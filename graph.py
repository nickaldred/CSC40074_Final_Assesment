from queue import PriorityQueue


class Graph():
    """
    Holds all the methods to create and tranverse the city graph.

    """
    def __init__ (self, size) -> None:
        self.graph = {}  #create empty adjacency list
        self.vertices_no = 0
        self.adjMatrix = [] #create empty adjacency matrix
        self.visited = [] #list for visited vertices for Dijkstra’s algorithm
        self.size = size #Amount of vertices in graph
        for i in range(size):
            self.adjMatrix.append([-1 for i in range(size)])

   
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
        Creates an edge adjacency list between the given vertices v1 and v2.
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

    def add_edge_matrix(self, v1, v2, w) -> None:
        """
        Creates an edge in the adjacency matrix between the two 
        given vertices with the weight provided.

        v1 = int or str - 1st vertex
        v2 = int or str - 2nd vertex
        e = int -  edge weight

        """
        v1 = self.convertLetter(v1)
        v2 = self.convertLetter(v2)
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = w
        self.adjMatrix[v2][v1] = w 


    def convertNo(self, num) -> str: 
        """
        Converts a number between 0-25 into a capital character from the 
        alphabet.

        Input:
        Int - "1"

        Output:
        Str - "B"
        """
        return(chr(num+65))


    def convertLetter(self, letter) -> int:
        """
        Converts a letter into a number between 0-25 for use in the 
        adjacency matrix.

        Input:
        Letter - str - 'A'

        Returns:
        Int - '0'
        """
        return(ord(letter)-65)   


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

    def create_city_matrix(self) -> None:
        self.add_edge_matrix('A', 'C', 15)
        self.add_edge_matrix('A', 'G', 11)
        self.add_edge_matrix('A', 'B', 2)
        self.add_edge_matrix('B', 'F', 6)
        self.add_edge_matrix('F', 'H', 1)
        self.add_edge_matrix('F', 'E', 5)
        self.add_edge_matrix('C', 'D', 18)
        self.add_edge_matrix('B', 'D', 5)
        self.add_edge_matrix('G', 'H', 3)
        self.add_edge_matrix('D', 'E', 6)
        self.add_edge_matrix('D', 'K', 11)
        self.add_edge_matrix('E', 'K', 12)
        self.add_edge_matrix('E', 'I', 13)
        self.add_edge_matrix('I', 'J', 5)
        self.add_edge_matrix('K', 'J', 37)

    def bfs(self, node, key) -> bool:
        """
        Performs a breadth-first search on the stored city graph using
        a provided starting node and search key.

        input:
        node - int or str - Starting node for search.
        key - int or str - Node to searched for

        Output:
        Bool - Idicates whether the node was found.

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




    def dfs(self, node, key, visited) -> bool:
        """
        Performs a depth-first search on the stored city graph using
        a provided starting node and search key.

        input:
        node - int or str - Starting node for search.
        key - int or str - Node to searched for
        visited - empty list - Empty list to store visted nodes.

        Output:
        Bool - Idicates whether the node was found.

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


         

    def dijkstra(self, start_vertex) -> dict:
        """
        Performs Dijkstra's algorithm using the given starting vertex
        on the city network graph stored in the object.

        Input:
        Int - starting vertex in graph

        Output:
        Dict - list of minimum distances between starting vertex and other
               vertices.
        """
        D = {v:float('inf') for v in range(self.size)}
        D[start_vertex] = 0
    
        pq = PriorityQueue()
        pq.put((0, start_vertex))
    
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)
    
            for neighbor in range(self.size):
                if self.adjMatrix[current_vertex][neighbor] != -1:
                    distance = self.adjMatrix[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D



    def find_min_distance(self, source, destination) -> int:
        """
        Finds the minimum distance from the source to all other nodes
        using jiskstra's algorithm. Then returns the minimum weight distance 
        for the given destination node.

        Input:
        source: str - representing city - 'A'
        destination: - str - representing city - 'A'

        Output:
        Int - Minimum weight distance between the given source and destination.
        """

        d = self.dijkstra(self.convertLetter(source))
        destination = self.convertLetter(destination)
        return(d[destination])



#graph.print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
#print ("Internal representation: ", graph.graph)

# graph = Graph(11)

# graph.create_city_graph()
# graph.create_city_matrix()
# # D = graph.dijkstra(0)

# # print(D)

# # for vertex in range(len(D)):
# #     print("Distance from vertex A to vertex", graph.convertNo(vertex), "is", D[vertex])

# print(graph.find_min_distance("J", "C"))

# #print(graph.search_vertex('A'))
#graph.print_formatted_graph()

# graph.covert_to_matrix()

# graph.printMatrix()

#print(graph.bfs("A", "a"))

# visited = set() # Set to keep track of visited nodes.
# print(graph.dfs("K", "A", visited, False))

#graph.print_city_list()

# print ("Internal representation: ", graph.graph)


