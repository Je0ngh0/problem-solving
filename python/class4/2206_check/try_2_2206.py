import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

MAX_DISTANCE = N * M + 1

start, end = (0, 0), (N, M)

result = [[[MAX_DISTANCE, MAX_DISTANCE] for _ in range(M)] for _ in range(N)]
result[start[0]][start[1]][0] = 1

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

queue = deque([start])
while queue:
    i, j = queue.popleft()
    avail_step = [
        (i + di[d], j + dj[d]) for d in range(4) if 0 <= i + di[d] < N and 0 <= j + dj[d] < M
    ]

    c_dist_p = result[i][j][0]
    c_dist_np = result[i][j][1]

    for ni, nj in avail_step:
        n_dist_p = result[ni][nj][0]
        n_dist_np = result[ni][nj][1]

        if arr[ni][nj] == 0:
            if c_dist_p + 1 < n_dist_p:
                result[ni][nj][0] = c_dist_p + 1
                queue.append([ni, nj])
            if c_dist_np + 1 < n_dist_np:
                result[ni][nj][1] = c_dist_np + 1
                queue.append([ni, nj])
        else:
            if c_dist_p + 1 < n_dist_np:
                result[ni][nj][1] = c_dist_p + 1
                queue.append([ni, nj])

result = min(result[N-1][M-1])

if result == MAX_DISTANCE:
    print(str(-1))
else:
    print(str(result))