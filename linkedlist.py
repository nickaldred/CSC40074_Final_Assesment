class Node:
    def __init__(self, log_in_id, item):
        self.id = log_in_id
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self) -> None:
        """
        Prints data of each element of the linked list
        List tranversal - Access all the nodes of the linked list
        
        """

        temp = self.head
        while (temp):
            print(str(temp.item) + " ", end="")
            temp = temp.next
        print("")


    def insert_at_end(self, log_in_id, new_data) -> None:
        """
        Appends element to the linked list.

        Input:
        log_in_id: int - id of new user or password - username and password id
                         must match.

        new_data: str - username or password to be stored in new node

        """

        new_node = Node(log_in_id, new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node

    
    def delete_node(self, position) -> None:
        """
        Deletes an element from the list at a particular position

        Input:
        posisition: Int
        
        """

        if self.head is None:
            return

        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key, search_type) -> None:
        """
        Searches for an element in a linked list
        
        Input:
        Key: int or str depending on type - Value to be searched for.
        Type: str - searchs for different types of data depending on value.
                    "item" - searchs for value in node, usually username
                    "id" - searchs for id of node

        """

        current = self.head

        while current is not None:
            if search_type == "item" and current.item == key:
                return current.id

            if search_type == "id" and current.id == key:
                return current.item

            current = current.next

        return False

