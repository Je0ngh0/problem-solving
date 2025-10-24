import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

v, e = map(int, input().strip().split())
k = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(e)]

graph = {key: [] for key in range(1, v+1)}

for start, end, value in arr:
    graph[start].append([end, value])

visited = [float('inf')] * (v+1)
start = k
queue = deque([start])
visited[start] = 0

while queue:
    current_position = queue.popleft()
    for next_position, value in graph[current_position]:
        temp_val = visited[current_position] + value
        if temp_val < visited[next_position]:
            queue.append(next_position)
            visited[next_position] = temp_val
for value in visited[1:]:
    if value == float('inf'):
        print("INF\n")
    else:
        print(str(value)+"\n")