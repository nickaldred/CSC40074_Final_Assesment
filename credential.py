from linkedlist import LinkedList
from linkedlist import Node



class Credential():
    def __init__(self) -> None:
        pass



    def validate(self, username, password) -> bool:
        """
        Validates the supplied username and password by using linear search
        against the 2 stored linked lists for username and password.

        Returns:
        Boolean type
        """

        #Searchs username link list and saves the ID it finds, if nothing is
        #found the id is set to False.
        __valid_id = self.username_list.search(username, "item")
        
        if __valid_id != False:
            #If the username was found use the saved ID to find the password
            #the password is then stored. 
            __valid_pass = self.password_list.search(__valid_id, "id")

            #If supplied password and stored password match return True
            if __valid_pass == password:
                return True
        
            else:
                return False
        
        else:
            return False

        


    def create_link_lists(self) -> None:
        """
        Creates 2 linked lists one for usernames and passwords.
        Each linked list contains 10 manually inputter usernames and passwords
        """
        #Create both linked lists
        self.username_list = LinkedList()
        self.password_list = LinkedList()
    
        #Set head of linked lists
        self.username_list.head = Node(1, "nickaldred")
        self.password_list.head = Node(1, "football")

        #Create rest of nodes for linked lists
        second_user = Node(2, "johnsmith")
        second_pass = Node(2, "golf")

        third_user = Node(3, "tomabbiss")
        third_pass = Node(3, "badminton")

        fourth_user = Node(4, "olivetree")
        fourth_pass = Node(4, "curling")

        fifth_user = Node(5, "johnquil")
        fifth_pass = Node(5, "tennis")

        sixth_user = Node(6, "aidabugg")
        sixth_pass = Node(6, "diving")

        seventh_user = Node(7, "eileensideways")
        seventh_pass = Node(7, "rugby")

        eigth_user = Node(8, "rodknee")
        eigth_pass = Node(8, "basketball")

        ninth_user = Node(9, "ritabook")
        ninth_pass = Node(9, "volleyball")

        tenth_user = Node(10, "rhodareport")
        tenth_pass = Node(10, "baseball")

        #Link each node in user linked list
        self.username_list.head.next = second_user
        second_user.next = third_user
        third_user.next = fourth_user
        fourth_user.next = fifth_user
        fifth_user.next = sixth_user
        sixth_user.next = seventh_user
        seventh_user.next = eigth_user
        eigth_user.next = ninth_user
        ninth_user.next = tenth_user

        #Link each node in password linked list
        self.password_list.head.next = second_pass
        second_pass.next = third_pass
        third_pass.next = fourth_pass
        fourth_pass.next = fifth_pass
        fifth_pass.next = sixth_pass
        sixth_pass.next = seventh_pass
        seventh_pass.next = eigth_pass
        eigth_pass.next = ninth_pass
        ninth_pass.next = tenth_pass


#Code used to test credential class

#cred = Credential()

#cred.create_link_lists()

#print(cred.validate("rhodarepor", "baseball"))

# print(cred.username_list.search("ritabook", "item"))
# print(cred.password_list.search(2, "id"))