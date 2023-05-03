class Graph:
    def __init__(self):
        self.node = []
        self.graph = []
        self.count = 0

    def add_node(self, data):
        if data in self.node:
            print("the node is already present in the graph>")
        else:
            self.node.append(data)
            self.count += 1
            for i in self.graph:
                i.append(0)
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
            print("The node is not present in the graph.")
        if v2 not in self.node:
            print("The node is not present in the graph.")
        else:
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)
            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1

    def delete_node(self, v):
        if v not in self.node:
            print("the node not present in the graph.")
        else:
            index = self.node.index(v)
            self.node.remove(v)
            for i in self.graph:
                i.pop(index)
            self.graph.pop(index)
            self.count -= 1

    def delete_edge(self, v1, v2):
        if v1 not in self.node:
            print("node is not present")
        if v2 not in self.node:
            print("node is not present.")
        else:
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)
            self.graph[index1][index2] = 0
            self.graph[index2][index1] = 0


mygraph = Graph()
mygraph.add_node("A")
mygraph.add_node("B")
mygraph.add_node("C")
mygraph.add_node("D")
mygraph.add_node("E")
mygraph.add_edge("A", "B")
mygraph.add_edge("A", "C")
mygraph.add_edge("B", "D")
mygraph.add_edge("C", "D")
mygraph.add_edge("E", "A")
mygraph.add_edge("B", "E")


print(mygraph.node)
mygraph.matrix_form()
mygraph.delete_edge("A", "B")
print(mygraph.node)
mygraph.matrix_form()