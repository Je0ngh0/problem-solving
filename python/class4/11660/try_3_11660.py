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
    for i in range(x+1):
        for j in range(y+1):
            if dp[i][j]:
                continue
            else:
                if j-1 < 0:
                    sub_sum1 = 0
                    overlab_sub_sum = 0
                else:
                    sub_sum1 = dp[i][j-1]

                if i-1 < 0:
                    sub_sum2 = 0
                    overlab_sub_sum = 0
                else:
                    sub_sum2 = dp[i-1][j]

                if i-1 >= 0 and j-1 >= 0:
                    overlab_sub_sum = dp[i-1][j-1]

                dp[i][j] = sub_sum1 + sub_sum2 - overlab_sub_sum + arr[i][j]
    return dp[x][y]        

for x1, y1, x2, y2 in xys:
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