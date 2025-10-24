import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().strip().split())

visited = [[0, False] for _ in range(10**6 + 1)]


start = n
queue = deque([start])
visited[start][1] = True

temp_result = 0
flag = False
while queue:  
    current_position = queue.popleft()
    graph = [
        (next_position, time) for next_position, time in ((current_position*2, 0), (current_position+1, 1), (current_position-1, 1)) if 0 <= next_position <= 10**6
    ]

    if current_position == k:
        temp_result = visited[k][0]
        flag = True

    for next_position, time in graph:
        new_travel_time = visited[current_position][0] + time
        if not visited[next_position][1]:
            visited[next_position] = [new_travel_time, True]
            if not flag:
                queue.append(next_position)
        elif new_travel_time < visited[next_position][0]:
            visited[next_position][0] = new_travel_time
            if not flag:
                queue.append(next_position)

print(str(temp_result))
    