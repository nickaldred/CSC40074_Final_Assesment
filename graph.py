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
        queue = []     #Initialize a queue.

        #Put starting node in the visited list and queue.
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 

            #Iterates over each neighbor of the node in the graph.
            for neighbour in self.graph[s[0]]:
                #Checks if neighbor is not in visited
                if neighbour not in visited:
                    #Checks if neighbor is equal to search key.
                    if neighbour[0] == key:
                        return(True)
                    #Add neighbor to Queue and visited.
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
        #If search key is in visited return true
        if key in visited:
            return(True)
        if node not in visited:

            #Add current node to visited
            visited.add(node)
            for neighbour in self.graph[node]:
                #Perform DFS on neighbor (Recursion)
                self.dfs(neighbour[0], key, visited)

                #If search key is in visited return true
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

        #List to keep shortest paths, all entries initialised to infinity
        D = {v:float('inf') for v in range(self.size)}
        D[start_vertex] = 0

        #Create a priority queue
        pq = PriorityQueue()
        #Put the starting vertex in the priority queue
        pq.put((0, start_vertex))

        #while the priority queue is not empty analyse each vertex
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            #set current vertex to visited
            self.visited.append(current_vertex)

            #Iterate over each of the current vertices neighbors
            for neighbor in range(self.size):
                if self.adjMatrix[current_vertex][neighbor] != -1:
                    #Find the distance between current vertex & neighbor
                    distance = self.adjMatrix[current_vertex][neighbor]
                    #If not visited compare old cost to new cost 
                    if neighbor not in self.visited:
                        #Find old cost and new cost
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            #If new cost lower the neighbor and its cost in the
                            #priority queue.
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D



    def find_min_distance(self, source, destination) -> int:
        """
        Finds the minimum distance from the source to all other nodes
        using Diskstra's algorithm. Then returns the minimum weight distance 
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


    def prims(self) -> list:
        """
        Finds the minimum spanning tree from the adjacency matrix stored in the
        object using prims algorithm. Returns the result in a list matrix.

        Output:
        List - Minimum spanning tree
        
        """
        # Define infinity variable
        infinity = float('inf')
        
        # Selected node list
        selected_nodes = [False for node in range(self.size)]

        # MST matrix
        result = [[0 for column in range(self.size)] 
                    for row in range(self.size)]
        
        index = 0
        
        # Keep looking while there are nodes that are not included in the MST.
        while(False in selected_nodes):

            # Use inifinity as minimum
            minimum = infinity

            # Start Node
            start = 0

            # End Node
            end = 0

            for i in range(self.size):
                # Inspect node if its part of the MST
                if selected_nodes[i]:
                    for j in range(self.size):
                        # If Node has a path to the ending Node AND is not already in the MST
                        if (self.adjMatrix[i][j]>0 and not selected_nodes[j] ):  
                            # If the weighted path is less than the minimum.
                            if self.adjMatrix[i][j] < minimum:
                                # Sets new minimum weight and the starting and end vertex.
                                minimum = self.adjMatrix[i][j]
                                start, end = i, j
            
            # Ending vertex is already selected.
            selected_nodes[end] = True

            # Fill the MST Adjacency Matrix.
            result[start][end] = minimum
            
            if minimum == infinity:
                result[start][end] = 0

            index += 1
            
            result[end][start] = result[start][end]

        return(result)


    def print_mst(self, mst) -> None:
        """
        Prints the minimum spanning inputted in a readable format for the user.

        Input:
        List matrix - lists within a list.

        Output:
        None
        """

        # Loops through MST list and the item in the MST and prints values.
        for i in range(len(mst)):
            for j in range(0+i, len(mst)):
                if mst[i][j] != 0:
                    print(f"{i} - {j}: {mst[i][j]}")



#graph.print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
#print ("Internal representation: ", graph.graph)

graph = Graph(11)

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

graph.create_city_matrix()
# # D = graph.dijkstra(0)
result = graph.prims()
graph.print_mst(result)
