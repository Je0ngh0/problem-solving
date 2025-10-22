import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

index_pairs = [(1, 2), (0, 2), (0, 1)]
dp = []
for i, seq in enumerate(arr):
    if i == 0:
        dp.append(seq)
        continue
    temp_seq = []
    for j, (x, y) in enumerate(index_pairs):
        temp_seq.append(seq[j] + min(dp[i-1][x], dp[i-1][y]))
    dp.append(temp_seq)

result = min(dp[-1])

print(f"{result}")