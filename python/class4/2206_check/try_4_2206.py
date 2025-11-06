import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]  # '0'과 '1' 문자 그대로 보관(메모리 절약)

    # dist[x][y][b]: (x,y)에 벽을 b번(0 또는 1) 부순 상태로 도달했을 때의 최단 거리
    dist = [[[0] * 2 for _ in range(M)] for __ in range(N)]

    dq = deque()
    dq.append((0, 0, 0))
    dist[0][0][0] = 1  # 시작 칸 포함

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while dq:
        x, y, b = dq.popleft()

        if x == N - 1 and y == M - 1:
            print(dist[x][y][b])
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 빈 칸으로 이동
                if grid[nx][ny] == '0' and dist[nx][ny][b] == 0:
                    dist[nx][ny][b] = dist[x][y][b] + 1
                    dq.append((nx, ny, b))
                # 벽이고 아직 부순 적이 없다면 한 번 부수고 이동
                elif grid[nx][ny] == '1' and b == 0 and dist[nx][ny][1] == 0:
                    dist[nx][ny][1] = dist[x][y][b] + 1
                    dq.append((nx, ny, 1))

    # 도착 불가
    print(-1)

if __name__ == "__main__":
    main()
