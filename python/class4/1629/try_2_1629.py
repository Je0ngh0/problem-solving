import sys

input = sys.stdin.readline
print = sys.stdout.write

a, b, c = map(int, input().strip().split())

temp = a % c
sub_temp = [temp]
for i in range(b):
    temp = (temp*a) % c

    if sub_temp[0] == temp:
        break
    else:
        sub_temp.append(temp)

result = sub_temp[b % len(sub_temp) - 1]

print(str(result))