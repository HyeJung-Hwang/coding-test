# 백준
# 1260

import sys
from collections import deque

input = sys.stdin.readline
v, e, start = map(int, input().split())

graph = [[]*(v + 1) for  i in range(v + 1)]
dfs_visited = [False]*(v + 1)
dfs_answer = []
bfs_answer = []
bfs_visited = [False]*(v + 1)

for i in range(e):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)
    graph[n].sort()
    graph[m].sort()

def dfs(
    graph,
    visited,
    v
):
    visited[v] = True
    global dfs_answer
    dfs_answer.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)
dfs(graph, dfs_visited, start)

def bfs(
    graph, 
    visited,
    v
):
    
    queue = deque([v])
    visited[v] = True
    global bfs_answer
    bfs_answer.append(v)
    while queue:
        next = queue.popleft()
        for i in graph[next]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                bfs_answer.append(i)

bfs(graph, bfs_visited, start)
print(*dfs_answer, sep=" ")
print(*bfs_answer, sep=" ")

