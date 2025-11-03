import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

def nqueen(n):
    def dfs(row, cols, diag1, diag2):
        if row == n:
            return 1
        count = 0
        available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
        while available:
            bit = available & -available
            available -= bit
            count += dfs(row + 1,
                         cols | bit,
                         (diag1 | bit) << 1,
                         (diag2 | bit) >> 1)
        return count
    return dfs(0, 0, 0, 0)

result = nqueen(n)

print(f"{result}")