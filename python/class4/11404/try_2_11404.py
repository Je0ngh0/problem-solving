n = int(input())
m = int(input())
edges = [list(map(int, input().strip().split())) for _ in range(m)]

MAX_FEE = 10**5
MAX_TOT_FEE = MAX_FEE * (n - 1) + 1

def floyd_warshall(n, edges):
    dist = [[MAX_TOT_FEE]*(n+1) for _ in range(n+1)]
    nxt = [[None]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dist[i][i] = 0
        nxt[i][i] = i

    for u, v, w in edges:
        temp_w = dist[u][v]
        if w < temp_w:
            dist[u][v] = w
            nxt[u][v] = v

    for k in range(1, n+1):
        dk = dist[k]
        for i in range(1, n+1):
            dik = dist[i][k]
            if dik == MAX_TOT_FEE:
                continue
            di = dist[i]
            nxi = nxt[i]
            for j in range(1, n+1):
                new_dij = dik + dk[j]
                if new_dij < di[j]:
                    di[j] = new_dij
                    nxi[j] = nxi[k]

    return dist, nxt

dist, nxt = floyd_warshall(n, edges)

for i in range(1, n+1):
    di = dist[i]
    for j in range(1, n+1):
        if di[j] == MAX_TOT_FEE:
            dist[i][j] = 0
    print(' '.join(map(str, di[1:])))
