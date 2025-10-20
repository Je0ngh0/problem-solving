import sys
from itertools import permutations

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().strip().split())
nums = map(int, input().strip().split())

for seq in sorted(permutations(nums, m)):
    print(f"{" ".join(map(str, seq))}\n")