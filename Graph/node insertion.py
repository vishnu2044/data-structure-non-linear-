class Graph:
    def __init__(self):
        self.node = []
        self.graph = []
        self.count = 0

    def add_node(self, data):
        if data in self.node:
            print("The node is already present in the graph>")
            return
        else:
            self.node.append(data)
            self.count += 1
            for n in self.graph:
                n.append(0)
            temp = []
            for i in range(self.count):
                temp.append(0)
            self.graph.append(temp)

    def matrix_form(self):
        for i in range(self.count):
            for j in range(self.count):
                print(self.graph[i][j], end="  ")
            print()


mygraph = Graph()
mygraph.add_node("A")
mygraph.add_node("B")
mygraph.add_node("C")
print(mygraph.node)
mygraph.matrix_form()