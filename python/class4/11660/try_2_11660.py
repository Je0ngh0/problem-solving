import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
xys = [list(map(lambda x: int(x) - 1, input().strip().split())) for _ in range(m)]

dp = [[False]*n for _ in range(n)]
dp[0][0] = arr[0][0]

def my_dp(arr, dp, x, y):
    if dp[x][y]:
        return dp[x][y]
    else:
        if y-1 < 0:
            sub_sum1 = 0
            overlab_sub_sum = 0
        else:
            sub_sum1 = my_dp(arr, dp, x, y-1)

        if x-1 < 0:
            sub_sum2 = 0
            overlab_sub_sum = 0
        else:
            sub_sum2 = my_dp(arr, dp, x-1, y)

        if x-1 >= 0 and y-1 >= 0:
            overlab_sub_sum = my_dp(arr, dp, x-1, y-1)
        dp[x][y] = sub_sum1 + sub_sum2 - overlab_sub_sum + arr[x][y]
        return dp[x][y]
    
for i, (x1, y1, x2, y2) in enumerate(xys):
    big_sum = my_dp(arr, dp, x2, y2)

    if y1 - 1 < 0:
        small_sum1 = 0
        overlap_sum = 0
    else:
        small_sum1 = my_dp(arr, dp, x2, y1-1)

    if x1 - 1 < 0:
        small_sum2 = 0
        overlap_sum = 0
    else:
        small_sum2 = my_dp(arr, dp, x1-1, y2)

    if x1 - 1 >= 0 and y1 - 1 >= 0:
        overlap_sum = my_dp(arr, dp, x1-1, y1-1)
        
    result = big_sum - small_sum1 - small_sum2 + overlap_sum
    print(f"{result}\n")

