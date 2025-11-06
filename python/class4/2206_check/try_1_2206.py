import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]


start, end = (0, 0), (N, M)

queue = deque([start])

result = [[None] * M for _ in range(N)]
result[start[0]][start[1]] = (1, True)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

while queue:
    i, j = queue.popleft()
    avail_step = [
        (i + di[d], j + dj[d]) for d in range(4) if 0 <= i + di[d] < N and 0 <= j + dj[d] < M
    ]

    for ni, nj in avail_step:
        if result[ni][nj] == None:
            if arr[ni][nj] == 0:
                result[ni][nj] = (result[i][j][0] + 1, result[i][j][1])
                queue.append((ni, nj))
            elif result[i][j][1]:
                result[ni][nj] = (result[i][j][0] + 1, False)
                queue.append((ni, nj))

if result[N-1][M-1] == None:
    print(str(-1))
else:
    print(str(result[N-1][M-1][0]))