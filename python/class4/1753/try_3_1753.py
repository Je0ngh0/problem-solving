import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
print = sys.stdout.write

V, e = map(int, input().strip().split())
k = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(e)]


graph = defaultdict(list)
for u, v, w in arr:
    graph[u].append((w, v))


start = k
queue = [(0, k)]
distances = [float('inf')] * (V+1)
distances[k] = 0

while queue:
    current_distance, node = heapq.heappop(queue)

    if current_distance > distances[node]:
        continue

    for weight, adjacent in graph[node]:
        adjacent_distance = current_distance + weight

        if adjacent_distance < distances[adjacent]:
            distances[adjacent] = adjacent_distance
            heapq.heappush(queue, (adjacent_distance, adjacent))

for result in distances[1:]:
    if result == float('inf'):
        print("INF\n")
    else:
        print(str(result)+"\n")