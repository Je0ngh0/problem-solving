import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
points = [tuple(map(int, input().strip().split())) for _ in range(n)]

def shoelace_area(points: list[tuple[float, float]]) -> float:
    pts = points
    n = len(pts)

    s = 0
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1

    area = 0.5 * abs(s)
    return area

area = shoelace_area(points)
area = round(area, 1)

print(str(area) + "\n")