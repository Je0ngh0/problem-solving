import sys

input = sys.stdin.readline
print = sys.stdout.write

a, b, c = map(int, input().strip().split())

temp = 1

for i in range(b):
    temp = (temp*a) % c

print(str(temp))