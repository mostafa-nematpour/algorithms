# complexity :  O(V+E)
# the number of vertices is O(V), whereas the number of edges is O(E).

from collections import deque

def node_is_target(node):
    return node[-1] == 'x'


def bfs(graph, start_node):
    search_queue = deque()
    search_queue += graph[start_node]

    searched = []
    while search_queue:
        node = search_queue.popleft()
        if not node in searched:
            if node_is_target(node):
                return node
            elif node in graph:
                search_queue += graph[node]
    return False


graph = {}

graph["me"] = ["mohammad", "ali", "parsa"]

graph["mohammad"] = ["mohammad-ali", "mahdi"]
graph["ali"] = ["mohammad", "robert"]
graph["parsa"] = ["mostafa", "my", "maria", "max"]

graph["mohammad-ali"] = []
graph["mahdi"] = []
graph["robert"] = []
graph["mostafa"] = []
graph["my"] = []
graph["max"] = []

print(bfs(graph, "me"))
