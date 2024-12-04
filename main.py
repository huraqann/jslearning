import collections

deque = collections.deque
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = []

    def add_edge(self, value1, value2):
        if value1 in self.nodes and value2 in self.nodes:
            self.nodes[value1].append(value2)

graph = Graph()
for node in ["A", "B", "C", "D", "E", "F", "G", "H"]:
    graph.add_node(node)

graph.add_edge("A", "B")
graph.add_edge("A", "D")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "G")
graph.add_edge("C", "D")
graph.add_edge("C", "F")
graph.add_edge("C", "H")
graph.add_edge("D", "E")
graph.add_edge("D", "F")
graph.add_edge("E", "F")
graph.add_edge("E", "G")
graph.add_edge("E", "H")
graph.add_edge("F", "G")
graph.add_edge("F", "H")
graph.add_edge("G", "H")

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (node, path) = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.nodes[node]:
            if neighbor == end:
                return path + [end]
            else:
                queue.append((neighbor, path + [neighbor]))
    return None

print(shortest_path(graph, "A", "G"))  # Output: ['A', 'C', 'D']