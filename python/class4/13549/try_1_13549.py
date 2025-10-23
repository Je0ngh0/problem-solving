import sys

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().strip().split())

visited = [[0, False] for _ in range((10**6 + 1))]

from collections import deque

start = n
visited[start][1] = True
queue = deque([start])

while queue:
    node = queue.popleft()

    graph = [
        (next_node, time) for next_node, time in ([node*2, 0], [node+1, 1], [node-1, 1]) if 0<= next_node <= 10**6
    ]

    if node == k:
        print(str(visited[k][0]))
        break

    for next_node, time in graph:
        if not visited[next_node][1]:
            queue.append(next_node)
            visited[next_node][0] = visited[node][0] + time
            visited[next_node][1] = True
        elif time == 0:
            queue.append(next_node)
            visited[next_node][0] = min(visited[node][0], visited[next_node][0])
    