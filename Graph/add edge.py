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

    def add_edge(self, v1, v2):
        if v1 not in self.node:
            print("The node is not present in the graph!!")
        if v2 not in self.node:
            print("The node is not present in the graph!!")
        else:
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)
            self.graph[index2][index1] = 1
            self.graph[index1][index2] = 1

    def addedge_directional(self, v1, v2):
        if v1 not in self.node:
            print("The node is not present in the graph!!")
        if v2 not in self.node:
            print("The node is not present in the graph!!")
        else:
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)
            self.graph[index1][index2] = 1

    def add_edge_weighted(self, v1, v2, cost):
        if v1 not in self.node:
            print("The node is not present in the graph!!")
        if v2 not in self.node:
            print("The node is not present in the graph!!")
        else:
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)
            self.graph[index1][index2] = cost
            self.graph[index2][index1] = cost



mygraph = Graph()
mygraph.add_node("A")
mygraph.add_node("B")
mygraph.add_node("C")
mygraph.add_node("D")
mygraph.add_node("E")
mygraph.add_edge("A", "B")
mygraph.addedge_directional("B", "C")
mygraph.add_edge_weighted("D", "E", 8)
mygraph.add_edge_weighted("D", "A", 5)

print(mygraph.node)
mygraph.matrix_form()