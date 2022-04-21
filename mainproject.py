import sys

from credential import Credential
from graph import Graph
from credential import Credential

class MainProject(Graph, Credential):
    def __init__(self) -> None:
        pass

    def startProgram(self) -> None:
        """
        Start the program and displays the log in terminal.
        
        """

        #Log in terminal and user input
        print("Welcome to the program, please enter your login details:")
        username = input("username: ")
        password = input("Password: ")

        print(username, password)

        try:
            program.menuDisplay()

        except:
            raise Exception("Error with menu")


    def menuDisplay(self) -> None:
        """
        Displays the menu for the functionality of the program
        """
        print("\nMenu:")
        print("1. Searching a city from the current city")
        print("2. The minimum distance between two cities")
        print("3. Finding the mininum spanning tree")
        print("4. Exit program")
        print("\n")
        menu_input = input("Please enter your choice from the menu: ") 

        try: 
            self.menuChoice(menu_input)
        except:
            raise Exception("Error with menu choice")


    def menuChoice(self, menu_input):
        """Allows the user to make a choice from the menu by taking an input"""

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
    program.startProgram()

