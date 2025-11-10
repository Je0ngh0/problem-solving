import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = tuple(map(int, input().strip().split()))

left, right = 0, n-1
ans = (arr[left], arr[right])
s = arr[left] + arr[right]
best = abs(s)

while left < right:
    s = arr[left] + arr[right]

    candi = abs(s)
    if candi < best:
        best = candi
        ans = (arr[left], arr[right])

    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        break

print(" ".join(map(str, ans)))