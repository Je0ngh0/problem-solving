from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    q = deque([start])
    max_dist, farthest_node = 0, start

    while q:
        node = q.popleft()
        for next_node, weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + weight
                q.append(next_node)
                if visited[next_node] > max_dist:
                    max_dist = visited[next_node]
                    farthest_node = next_node
    return farthest_node, max_dist


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))  # 무방향 그래프

# 1. 임의의 노드(예: 1)에서 가장 먼 노드를 찾는다
farthest, _ = bfs(1)

# 2. 그 노드에서 다시 BFS를 돌려 가장 먼 거리(= 지름)를 구한다
_, diameter = bfs(farthest)

print(diameter)
