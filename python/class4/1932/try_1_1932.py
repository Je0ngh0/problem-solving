import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

dp = [arr[0]]
ds = [0, -1]
for i in range(1, n):
    temp_arr = []
    for j, cv in enumerate(arr[i]):
        pre_len = len(arr[i-1])
        temp_num = 0
        for d in ds:
            if 0 <= j + d < pre_len:
                if dp[i-1][j+d] > temp_num:
                    temp_num = dp[i-1][j+d]
        temp_arr.append(temp_num+cv)
    dp.append(temp_arr)

print(f"{max(dp[-1])}")