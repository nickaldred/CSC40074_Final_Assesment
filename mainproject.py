from credential import Credential
from graph import Graph
from credential import Credential

class MainProject(Graph, Credential):
    def __init__(self) -> None:
        pass

    def login(self) -> None:
        """
        Start the program and displays the log in terminal.
        
        """

        #Create username and password linked lists using inherited method
        self.create_link_lists()

        #Log in terminal and user input
        print("Welcome to the program, please enter your login details:")
        username = input("username: ")
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
        graph = Graph()
        graph.create_city_graph()
        graph.print_city_list()

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
                pass
            elif int(menu_input) == 2:
                pass
            elif int(menu_input) == 3:
                pass
            elif int(menu_input) == 4:
                menuchoice = False
                
            else:
                print("please enter a valid menu choice.")
                menu_input = input("\nPlease enter your choice from the menu: ") 



  


if __name__ == "__main__":
    program = MainProject()
    program.login()

