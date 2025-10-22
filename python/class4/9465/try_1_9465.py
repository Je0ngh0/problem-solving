import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
cases = dict()
for i in range(t):
    n = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(2)]
    cases[f"case{i}"] = {"n": n, "arr": arr}

def my_dp(n, arr):
    if n == 1:
        return max(arr[0][0], arr[1][0])
    
    dp = [
        [arr[0][0], arr[1][0] + arr[0][1]],
        [arr[1][0], arr[0][0] + arr[1][1]],
    ]

    for i in range(2, n):
        if dp[1][i-2] > dp[1][i-1]:
            dp[0].append(dp[1][i-2] + arr[0][i])
        else:
            dp[0].append(dp[1][i-1] + arr[0][i])

        if dp[0][i-2] > dp[0][i-1]:
            dp[1].append(dp[0][i-2] + arr[1][i])
        else:
            dp[1].append(dp[0][i-1] + arr[1][i])

    result = max(dp[0][-1], dp[1][-1])
    return result

for case in cases.values():
    n, arr = case.values()
    print(f"{my_dp(n, arr)}\n")