

class AdjNode:
    def __init__(self, vertex, weight):
        """
        Used to create a node object for a linked list.
        vertext = current vertex
        weight = weight of edge to next vertex
        next = pointer to next vertex
        returns = none
        """
        self.vertex = vertex
        self.weight = weight
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d, weight):
        s = self.convert_letter(s)
        d = self.convert_letter(d)
        node = AdjNode(d, weight)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s, weight)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + self.convert_no(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {self.convert_no(temp.vertex)}, w:{temp.weight}", end="")

                temp = temp.next
            print(" \n")

    def convert_no(self, num): 
        return(chr(num+97))
    
    def convert_letter(self,letter):
        return(ord(letter)-97)



if __name__ == "__main__":
    V = 4

    # Create graph and edges
    
    graph = Graph(V)
    graph.add_edge('a', 'b', 3)
    graph.add_edge('a', 'c', 4)
    graph.add_edge('a', 'd', 2)
    graph.add_edge('b', 'c', 1)

    graph.print_agraph()