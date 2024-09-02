from collections import deque


def bfs(graph:list, visited: list,start: int):
    queue = deque([start])
    visited[start] = True
    while queue:
        next = queue.popleft()
        for i in graph[next]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    []
]
N = len(graph)
visited = [False] * N
