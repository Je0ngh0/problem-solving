import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
points = [tuple(map(int, input().strip().split())) for _ in range(n)]

def tri_area(p1: tuple[int], p2: tuple[int], p3: tuple[int]) -> float:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    result = abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3) / 2

    return result

fixed_point = points[0]

area_sum = 0
for i in range(1, n-1):
    p2 = points[i]
    p3 = points[i+1]

    area_sum += tri_area(fixed_point, p2, p3)

result = round(area_sum, 1)
print(str(result) + "\n")