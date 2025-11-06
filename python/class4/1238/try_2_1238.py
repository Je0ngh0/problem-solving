import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

n, m, x = map(int, input().strip().split())

f_graph = [[] for _ in range(n+1)]
r_graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, weight = map(int, input().strip().split())
    f_graph[start].append((weight, end))
    r_graph[end].append((weight, start))

MAX_TIME = 100
MAX_TOT_TIME = 100 * (n-1) + 1

def dijkstra(start, graph):
    tot_times = [MAX_TOT_TIME] * (n+1)
    tot_times[start] = 0

    c_time = tot_times[start]
    queue = [(c_time, start)]

    visited = [False] * (n + 1)

    while queue:
        c_time, node = heapq.heappop(queue)

        # if node == end:
        #     return tot_times

        if visited[node]:
            continue
        visited[node] = True

        for a_time, adjacent in graph[node]:
            new_time = c_time + a_time

            if new_time < tot_times[adjacent]:
                tot_times[adjacent] = new_time
                heapq.heappush(queue, (new_time, adjacent))

    return tot_times

x_to_i = dijkstra(x, f_graph)
i_to_x = dijkstra(x, r_graph)

result = 0
for i in range(1, n+1):
    result = max(result, x_to_i[i] + i_to_x[i])

print(f"{result}")