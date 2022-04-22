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


    def insert_at_end(self, new_data) -> None:
        """
        Appends element to the linked list.

        """

        new_node = Node(new_data)

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

    def search(self, key, type) -> None:
        """
        Searches for an element in a linked list

        """

        current = self.head

        while current is not None:
            if type == "item" and current.item == key:
                return current.id

            if type == "id" and current.id == key:
                return current.item

            current = current.next

        return False

