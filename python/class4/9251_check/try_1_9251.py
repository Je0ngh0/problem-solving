import sys

input = sys.stdin.readline
print = sys.stdout.write

arr = [input().strip() for _ in range(2)]
n, m = len(arr[0]), len(arr[1])

# 행은 n+1, 열은 m+1
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[0][i-1] == arr[1][j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(f"{dp[n][m]}")