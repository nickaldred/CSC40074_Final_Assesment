from credential import Credential
from graph import Graph
from credential import Credential

class MainProject(Graph, Credential):
    def __init__(self) -> None:
        self.graph = {}  #create empty adjacency list.
        self.vertices_no = 0
        self.adj_matrix = [] #Create empty adjacency matrix.
        self.krusk_graph = [] #Create an empty list for kruskals graph.
        self.visited = [] #List for visited vertices for Dijkstra’s. 
        self.size = 11 #Amount of vertices in graph.
        #Sets all values in adjacency matrix to -1.
        for i in range(self.size):
            self.adj_matrix.append([-1 for i in range(self.size)])


    def login(self) -> None:
        """
        Start the program and displays the log in terminal.
        
        """

        #Create username and password linked lists using inherited 
        # method.
        self.create_link_lists()

        #Log in terminal and user input.
        print("\nWelcome to the program, please enter your login details:")
        username = input("Username: ")
        password = input("Password: ")

        #Validate username and password using inherited method.
        if self.validate(username, password):

            try:
                program.showFunctionality()

            except:
                raise Exception("Error with menu")
        else:
            print("Incorrect username or password")


    def showFunctionality(self) -> None:
        """
        Displays a list of citys & the menu for the functionality of 
        the program.
        """
        #Creates the various interpretations of the graphs needed for 
        #the algorithms.

        self.create_city_graph()
        self.create_city_matrix()
        self.create_krusk_graph()

        #Prints the list of citys for the user to see.
        self.print_city_list()

        #Displays Menu
        #While loop to keep the program running untill the user decides 
        #to exit.
        menuchoice = True
        while menuchoice == True:
            print("\nMenu:")
            print("1. Searching a city from the current city")
            print("2. The minimum distance between two cities")
            print("3. Finding the mininum spanning tree")
            print("4. Exit program")
            print("\n")
            menu_input = input("Please enter your choice from the menu: ") 

            try: 
                menuchoice = self.menu_choice(menu_input)
            except:
                raise Exception("Error with menu choice")


    def menu_choice(self, menu_input) -> bool:
        """
        Allows the user to make a choice from the menu by taking an 
        input.

        Input:
        menu_input: int between 1-4 
        
        """

        #Decides what method to run based on users input.
        if int(menu_input) == 1:
            return(self.search_city())
        elif int(menu_input) == 2:
            return(self.find_min_distance_interface())
        elif int(menu_input) == 3:
            return(self.display_mst_algos())
        elif int(menu_input) == 4:
            return(False)
            
        else:
            print("please enter a valid menu choice.\n")
            return(True)


    def exit_menu(self) -> bool:
        """
        Allows the user to repeat function or exit the feature.
        
        Input:
        exit_menu_choice: int - menu choice to repeat 

        Output:
        Boolean
        
        """

        exit_log = input("\nEnter any key to continue or Q to Exit: ")
        if exit_log == "q" or exit_log == "Q":
            return(False)
        else:
            return(True)



    def search_city(self) -> bool:
        """
        Allows the user to search the city graph using DFS or BFS
        from a source and destination entered via the keyboard.

        Returns:
        Boolean
        
        """

        #Takes the users input via keybaord entry.
        source = input("\nPlease enter source city: ")
        destination = input("Please enter destination city: ")
        
        #Searchs the graph make sure the source input entered is a 
        #valid vertex.
        if self.search_vertex(source) == False:
            (print("\nSource city doesnt exist, please try again"))
            return(True)

        #User decides via keyboard input which search type to use BFS 
        # or DFS.
        search_type = input("Please enter search type 'BFS' or 'DFS': ")

        if search_type == "dfs" or search_type == "DFS":
            visited = set() # Set to keep track of visited nodes.
            result = self.dfs(source, destination, visited)
        elif search_type == "BFS" or search_type == "bfs":
            result = self.bfs(source, destination)
        else:
            print("\nPlease enter a correct search type")
            return(1)

        #Prints the results of the search to the command line.
        if result == True:
            print(f"\nSource: {source}, Destination: {destination}",
                    "--> Reachable")
        else: 
            print(f"\nSource: {source}, Destination: {destination}",
                    " --> Unreachable")

        #Displays the exit menu.
        return(self.exit_menu())


    def find_min_distance_interface(self) -> bool:
        """
        Allows the user to find the minimum distance between two given
        citys. 

        Returns:
        Boolean
        
        """

        #Takes the users input via keybaord entry.
        source = input("\nPlease enter source city: ")
        destination = input("Please enter destination city: ")
        
        #Searchs the graph make sure the source and destination
        #input entered is a valid vertex.
        if self.search_vertex(source) == False:
            (print("\nSource city doesnt exist, please try again"))
            return(True)
        
        elif self.search_vertex(destination) == False:
            (print("\nDestination city doesnt exist, please try again"))
            return(True)

        else:
            #Implements find_min_distance and Dijkstra’s method to find
            #the shortest distance between two vertices.
            distance = self.find_min_distance(source, destination)
            print(f"\nSource: {source}, Destination: {destination}",
                    f" --> {distance}")
            self.visited = []

        
        #Displays the exit menu.
        return(self.exit_menu())

    
    def display_mst_algos(self) -> bool:
        """
        Allows the user to run the spanning tree method which runs two 
        threads. One for Prim's algorithm and the other for Kruskal's 
        algorithm. 

        Returns:
        Boolean
        
        """
        self.spanningTree()
        #Displays the exit menu.
        return(self.exit_menu())


if __name__ == "__main__":
    program = MainProject()
    program.login()

