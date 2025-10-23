import sys

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().strip().split())
wvs = [tuple(map(int, input().strip().split())) for _ in range(n)]
weight_sum = sum(map(lambda x: x[0], wvs))

dp = [[0 for _ in range(weight_sum+1)] for _ in range(n+1)]

from itertools import combinations

combss = []
for i in range(1, n+1):
    combss.append(list(combinations(wvs, i)))

for item_num, combs in enumerate(combss):
    item_num += 1
    for comb in combs:
        w = sum(map(lambda x: x[0], comb))
        v = sum(map(lambda x: x[1], comb))
        dp[item_num][w] = max(dp[item_num][w], v)

temp = 0
for item_num in range(1, n+1):
    temp = 0
    for weight in range(weight_sum+1):
        if dp[item_num][weight] == 0 :
            if temp == 0:
                dp[item_num][weight] = dp[item_num-1][weight]
            elif temp != 0:
                dp[item_num][weight] = temp
        else:
            temp = dp[item_num][weight]

print(f"{dp[n][k]}\n")
