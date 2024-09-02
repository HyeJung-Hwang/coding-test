# 재귀를 이용한 구현

def dfs(
        graph: list,
        visited: list,
        v: int
):
    visited[v] = True
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, visited, i)





