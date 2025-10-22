import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
xys = [list(map(lambda x: int(x) - 1, input().strip().split())) for _ in range(m)]

for i, (x1, y1, x2, y2) in enumerate(xys):
        new_arr = [row[y1:y2+1] for row in arr[x1:x2+1]]
        print(str(sum(sum(row) for row in new_arr)) + "\n")


# print(f'''{n}
# {m}
# {arr}
# {xys}''')