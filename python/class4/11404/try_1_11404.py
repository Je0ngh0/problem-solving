import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())
arr = [tuple(map(int, input().strip().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for seq in arr:
    graph[seq[0]].append((seq[2], seq[1]))

tot_pricess = []
for i in range(1, n+1):
    start = i
    queue = [(0, start)]
    tot_prices = [float("inf")] * (n + 1)
    tot_prices[start] = 0

    while queue:
        c_price, node = heapq.heappop(queue)

        if c_price > tot_prices[node]:
            continue

        for a_price, adjacent in graph[node]:
            tot_price = a_price + c_price
            if tot_price < tot_prices[adjacent]:
                tot_prices[adjacent] = tot_price
                heapq.heappush(queue, (tot_price, adjacent))
                
    tot_prices = [0 if x == float("inf") else x for x in tot_prices]
    tot_pricess.append(tot_prices)

for seq in tot_pricess:
    print(' '.join(map(str, seq[1:]))+"\n")