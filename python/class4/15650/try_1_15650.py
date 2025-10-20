import sys
from itertools import combinations

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().strip().split())

nums = range(1, n+1)
combs = combinations(nums, m)

for comb in combs:
    print(f"{" ".join(map(str, comb))}\n")

