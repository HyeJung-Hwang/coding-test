# 이것이 취업을 위한 코딩테스트다.
# 음료수 얼려 먹기

N,M = map( int, input().split())
N, M = int(N), int(M)

graph = [ ]
for i in range(N):
     graph.append(list(map(int,input())))

# 상하좌우 움직임 관리
moves = [
    (-1,0), #상
    (1,0), # 하 
    (0,-1), # 좌
    (0,1) # 우
]

def dfs( i,j):
    # 재귀 탈출 조건
    if i <= -1 or i >= N or j <= -1 or j >= N:
         return False
    if graph[i][j] == 0:
         graph[i][j] = 1
         dfs(i - 1, j)
         dfs(i, j + 1)
         dfs(i + 1, j)
         dfs(i,j - 1)
         # 현재 위치에서 dfs가 모두 수행되었다는 의미의 True
         return True

count = 0
for i in range(N):
    for j in range(M):
        # 현재 위치엑서 dfs를 수헹헤서 True/False 따진 후에 +1
            if dfs( i, j) == True:
                 count += 1
print(count)