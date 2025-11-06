import sys

input = sys.stdin.readline
print = sys.stdout.write

MAX_TIME = 10 ** 4

def bellman_ford(N, edges):
    MAX_TOT_TIME = MAX_TIME * (N - 1) + 1
    times = [MAX_TOT_TIME] * (N + 1)
    times = [0] * (N + 1)

    source = 0
    times[source] = 0

    for _ in range(N-1):
        updated = False

        for u, v, w in edges:
            new_time = times[u] + w
            if times[u] != MAX_TOT_TIME and new_time < times[v]:
                times[v] = new_time
                updated = True
        if not updated:
            break
    
    for u, v, w in edges:
        new_time = times[u] + w
        if times[u] != MAX_TOT_TIME and new_time < times[v]:
            return "YES"
        
    return "NO"

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().strip().split())
    
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        edges.append((u, v, w))
        edges.append((v, u, w))
    for _ in range(W):
        u, v, w = map(int, input().strip().split())
        edges.append((u, v, -w))
    for i in range(1, N+1):
        edges.append((0, i, 0))

    print(bellman_ford(N, edges)+"\n")