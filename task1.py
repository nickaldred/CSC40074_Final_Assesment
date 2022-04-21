

class AdjNode:
    def __init__(self, vertex, weight) -> None:
        """
        Used to create a node object for a linked list.
        Input:
        vertex = current vertex
        weight = weight of edge to next vertex
        next = pointer to next vertex
        returns = none
        """
        self.vertex = vertex
        self.weight = weight
        self.next = None


class Graph:
    """
    Used to create a graph object for an adjacency list.
    Input:
    num = number of vertices
    """
    def __init__(self, num) -> None:
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d, weight) -> None:
        """
        Adds an edge to the graph by creating a link list node and
        adding that to the graph.

        Input:
        s = cuurent node
        d = next node
        weight = weight of edge
        """
        s = self.convert_letter(s)
        d = self.convert_letter(d)
        node = AdjNode(d, weight)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s, weight)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self) -> None:
        """
        Prints the graph in a adjacency list format.
        
        """
        for i in range(self.V):
            print("Vertex " + self.convert_no(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {self.convert_no(temp.vertex)}, w:{temp.weight}", end="")

                temp = temp.next
            print(" \n")


    def convert_no(self, num) -> str:
        """
        Converts a number between 1-26 into its equivalent in the alphabet.
        Returns the letter as a string.
        """
        return(chr(num+97))

    
    def convert_letter(self,letter) -> int:
        """
        Converts a letter from the alphabet in its equivalent number between 
        1-26.
        Returns the number as an int.
        """

        return(ord(letter)-97)



if __name__ == "__main__":
    #Number of vertices
    V = 11

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge('a', 'c', 15)
    graph.add_edge('a', 'g', 11)
    graph.add_edge('a', 'b', 2)
    graph.add_edge('b', 'f', 6)
    graph.add_edge('f', 'h', 1)
    graph.add_edge('f', 'e', 5)
    graph.add_edge('c', 'd', 18)
    graph.add_edge('b', 'd', 5)
    graph.add_edge('g', 'h', 3)
    graph.add_edge('d', 'e', 9)
    graph.add_edge('d', 'k', 11)
    graph.add_edge('e', 'k', 12)
    graph.add_edge('e', 'i', 13)
    graph.add_edge('i', 'j', 5)
    graph.add_edge('k', 'j', 37)

    #Prints adjacency list
    graph.print_agraph()