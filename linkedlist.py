class Node:
    """
    Creates a node to be used in the linked list.

    Input:
    log_in_ID: INT - ID to find node
    item - String - contains username or password of user.
    """
    def __init__(self, log_in_id, item) -> None:
        self.id = log_in_id
        self.item = item
        self.next = None


class LinkedList:
    """
    Creates an empty linked list.
    """
    def __init__(self):
        self.head = None

    def search(self, key, search_type) -> None:
        """
        Searches for an element in a linked list.
        
        Input:
        Key: int or str depending on type - Value to be searched for.
        Type: str - searchs for different types of data depending on 
                    value.
                    "item" - searchs for value in node, usually 
                            username.
                    "id" - searchs for id of node.

        """

        current = self.head

        while current is not None:
            if search_type == "item" and current.item == key:
                return current.id

            if search_type == "id" and current.id == key:
                return current.item

            current = current.next

        return False

