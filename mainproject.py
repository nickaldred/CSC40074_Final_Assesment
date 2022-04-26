from credential import Credential
from graph import Graph
from credential import Credential

class MainProject(Graph, Credential):
    def __init__(self) -> None:
        self.graph = {}  #create empty adjacency list
        self.vertices_no = 0
        self.adjMatrix = [] #create empty adjacency matrix
        self.visited = [] #list for visited vertices for Dijkstra’s algorithm
        self.size = 11 #Amount of vertices in graph
        for i in range(self.size):
            self.adjMatrix.append([-1 for i in range(self.size)])

    def login(self) -> None:
        """
        Start the program and displays the log in terminal.
        
        """

        #Create username and password linked lists using inherited method
        self.create_link_lists()

        #Log in terminal and user input
        print("\nWelcome to the program, please enter your login details:")
        username = input("Username: ")
        password = input("Password: ")

        #validate username and password using inherited method
        if self.validate(username, password):

            try:
                program.showFunctionality()

            except:
                raise Exception("Error with menu")
        else:
            print("Incorrect username or password")


    def showFunctionality(self) -> None:
        """
        Displays a list of citys & the menu for the functionality of the 
        program
        """
        #Create city network graph and then print a list of the citys.

        self.create_city_graph()
        self.create_city_matrix()
        self.print_city_list()

        #Displays Menu
        print("\nMenu:")
        print("1. Searching a city from the current city")
        print("2. The minimum distance between two cities")
        print("3. Finding the mininum spanning tree")
        print("4. Exit program")
        print("\n")
        menu_input = input("Please enter your choice from the menu: ") 

        try: 
            self.menu_choice(menu_input)
        except:
            raise Exception("Error with menu choice")


    def menu_choice(self, menu_input) -> None:
        """
        Allows the user to make a choice from the menu by taking an input
        Input:
        menu_input: int between 1-4 
        
        """

        menuchoice = True
        #While loop to keep the program running untill the user decides to exit.
        while menuchoice == True:
            if int(menu_input) == 1:
                menu_input = self.search_city()
            elif int(menu_input) == 2:
                menu_input = self.find_min_distance_interface()
            elif int(menu_input) == 3:
                pass
            elif int(menu_input) == 4:
                menuchoice = False
            elif int(menu_input) == 0:
                menuchoice = True
                
            else:
                print("please enter a valid menu choice.")
                menu_input = input("\nPlease enter your choice from the menu: ") 


    def search_city(self) -> int:
        """
        Allows the user to search the city graph using DFS or BFS
        from a source and destination entered via the keyboard.

        Returns:
        Int = Int which decides what menu option to use from menu_choice 
        
        """

        #Takes the users input via keybaord entry
        source = input("\nPlease enter source city: ")
        destination = input("Please enter destination city: ")
        
        #Searchs the graph make sure the source input entered is a valid vertex
        if self.search_vertex(source) == False:
            (print("Source city doesnt exist, please try again"))
            return(1)

        #User decides via keyboard input which search type to use BFS or DFS
        search_type = input("Please enter search type 'BFS' or 'DFS': ")

        if search_type == "dfs" or search_type == "DFS":
            visited = set() # Set to keep track of visited nodes.
            result = self.dfs(source, destination, visited)
        elif search_type == "BFS" or search_type == "bfs":
            result = self.bfs(source, destination)
        else:
            print("\nPlease enter a correct search type")
            return(1)

        #Prints the results of the search to the command line
        if result == True:
            print(f"\nSource: {source}, Destination: {destination}",
                    "--> Reachable")
        else: 
            print(f"\nSource: {source}, Destination: {destination}",
                    " --> Unreachable")

        #Displays exit menu
        return(self.exit_menu(1))


    def find_min_distance_interface(self) -> int:
        """
        Allows the user to find the minimum distance between two given
        citys. 

        Returns:
        Int = Int which decides what menu option to use from menu_choice 
        
        """

        #Takes the users input via keybaord entry
        source = input("\nPlease enter source city: ")
        destination = input("Please enter destination city: ")
        
        #Searchs the graph make sure the source and destination
        #input entered is a valid vertex
        if self.search_vertex(source) == False:
            (print("Source city doesnt exist, please try again"))
            return(2)
        
        elif self.search_vertex(destination) == False:
            (print("Destination city doesnt exist, please try again"))
            return(2)

        else:
            #Implements find_min_distance and Dijkstra’s method to find
            #the shortest distance between two vertices.
            distance = self.find_min_distance(source, destination)
            print(f"\nSource: {source}, Destination: {destination}",
                    f" --> {distance}")
            self.visited = []

        
        #Displays exit menu
        return(self.exit_menu(2))


    def exit_menu(self, exit_menu_choice) -> int:
        """
        Allows the user to repeat function or exit the feature.
        
        Input:
        exit_menu_choice: int - menu choice to repeat 

        Output:
        Int: to determine if repeat function or exit to menu
        
        """

        exit_log = input("\nEnter any key to continue or Q to Exit: ")
        if exit_log == "q" or exit_log == "Q":
            return(0)
        else:
            return(exit_menu_choice)

         

  


if __name__ == "__main__":
    program = MainProject()
    program.login()

