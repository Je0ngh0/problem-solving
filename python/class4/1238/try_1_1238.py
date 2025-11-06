import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

n, m, x = map(int, input().strip().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, weight = map(int, input().strip().split())
    graph[start].append((weight, end))

MAX_TIME = 100
MAX_TOT_TIME = 100 * (n-1) + 1

def dijkstra(start, end, graph):
    tot_time = [MAX_TOT_TIME] * (n+1)
    tot_time[start] = 0

    c_time = tot_time[start]
    queue = [(c_time, start)]

    visited = [False] * (n+1)

    while queue:
        c_time, node = heapq.heappop(queue)

        if node == end:
            return tot_time[end]

        if visited[node]:
            continue
        visited[node] = True

        for a_time, adjacent in graph[node]:
            new_time = c_time + a_time
            if  new_time < tot_time[adjacent]:
                tot_time[adjacent] = new_time
                heapq.heappush(queue, (new_time, adjacent))

results = [0] * (n + 1)
for i in range(1, n+1):
    results[i] = dijkstra(i, x, graph) + dijkstra(x, i, graph)

print(str(max(results)))