import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

V = int(input())

graph = [[] for _ in range(V+1)]
for i in range(1, V+1):
    seq = deque(map(int, input().strip().split()))
    
    start = seq.popleft()
    while seq:
        adjacent = seq.popleft()
        if adjacent == -1:
            break
        dist = seq.popleft()

        graph[start].append((dist, adjacent))

def my_bfs(start: int, graph: list[list[tuple[int, int]] | None]) -> list[int]:
    visited = [False] * (V + 1)
    visited[start] = True

    queue = deque([(0, start)])

    result = [0, 1]

    while queue:
        tot_dist, node = queue.popleft()

        for dist, adjacent in graph[node]:
            if not visited[adjacent]:
                new_tot_dist = tot_dist + dist
                queue.append((new_tot_dist, adjacent))
                visited[adjacent] = True

                if result[0] < new_tot_dist:
                    result[0] = new_tot_dist
                    result[1] = adjacent

    return result

start = 1
_, farthest_node = my_bfs(start, graph)
result, _ = my_bfs(farthest_node, graph)

print(str(result))