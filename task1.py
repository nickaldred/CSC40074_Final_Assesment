

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
        node = AdjNode(d, weight)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s, weight)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}, {temp.weight}", end="")

                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges

    #a = 1
    #b = 2
    #c = 3
    #d = 4
    #e = 5
    #f = 6
    #g = 7
    #h = 8
    #i = 9
    #j = 10
    #k = 11
    graph = Graph(V)
    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 2, 4)
    graph.add_edge(0, 3, 2)
    graph.add_edge(1, 2, 1)

    graph.print_agraph()