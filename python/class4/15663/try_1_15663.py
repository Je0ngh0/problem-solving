from itertools import permutations

n, m = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))


arr = sorted(list(set(permutations(nums, m))))
for seq in arr:
    print(" ".join(map(str, seq)))