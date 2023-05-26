from collections import deque

# Graph given in Adjacency-List
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end=' ')

        # Reversed order traversal. Big number Node go to the stack first
        for i in graph[cur_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (len(graph) + 1)

bfs(graph, 1, visited)