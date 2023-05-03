def add_node(node):
    if node in graph:
        print("The node is already present in the graph.")
    else:
        graph[node] = []


def add_edge(node1, node2):
    if node1 not in graph:
        print("the node is not present in the graph.")
    if node2 not in graph:
        print("the node is not present in the graph.")
    else:
        graph[node1].append(node2)
        graph[node2].append(node1)

def dfs(node, visited, graph):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i, visited, graph)


visited = set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("B", "E")
add_edge("D", "E")
add_edge("C", "D")
print(graph)
dfs("A", visited, graph)


