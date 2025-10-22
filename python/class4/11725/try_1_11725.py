import sys
from collections import deque

n = int(input())
nodes = [list(map(int, input().strip().split())) for _ in range(n-1)]

graph = {
    key: [] for key in range(n+1)
}
tree = {
    key: [] for key in range(n+1)
}

for x, y in nodes:
    graph[x].append(y)
    graph[y].append(x)

root = 1
tree[1] = 1
queue = deque([root])
visited = [False for _ in range(n+1)]

while queue:
    node = queue.popleft()
    visited[node] = True
    for neighborhood in graph[node]:
        if not visited[neighborhood]:
            queue.append(neighborhood)
            tree[neighborhood] = node

for key, value in tree.items():
    if not key <= 1:
        print(value)