import sys

# input = sys.stdin.readline
# print = sys.stdout.write

n = int(input())
liquids = tuple(map(int, input().strip().split()))

liqiud_a_index = 0
liquid_b_index = n-1
characteristic = liquids[liqiud_a_index] + liquids[liquid_b_index]
visited = {(liqiud_a_index, liquid_b_index)}

stack = [(liqiud_a_index, liquid_b_index, characteristic)]

result = (liqiud_a_index, liquid_b_index, abs(characteristic))
while stack:
    liqiud_a_index, liquid_b_index, characteristic = stack.pop()

    if characteristic < 0:
        dab = [(0, 1), (1, 0)]
        for a, b in dab:
            nxt_liqiud_a_index = liqiud_a_index + a
            nxt_liquid_b_index = liquid_b_index + b
            if nxt_liquid_b_index < n and nxt_liqiud_a_index != nxt_liquid_b_index and (nxt_liqiud_a_index, nxt_liquid_b_index) not in visited:
                nxt_characteristic = liquids[nxt_liqiud_a_index] + liquids[nxt_liquid_b_index]
                stack.append((nxt_liqiud_a_index, nxt_liquid_b_index, nxt_characteristic))
                visited.add((nxt_liqiud_a_index, nxt_liquid_b_index))

                if abs(nxt_characteristic) <= result[2]:
                    result = (nxt_liqiud_a_index, nxt_liquid_b_index, abs(nxt_characteristic))
    elif characteristic > 0:
        dab = [(0, -1), (-1, 0)]

        for a, b in dab:
            nxt_liqiud_a_index = liqiud_a_index + a
            nxt_liquid_b_index = liquid_b_index + b
            if nxt_liqiud_a_index >= 0 and nxt_liqiud_a_index != nxt_liquid_b_index and (nxt_liqiud_a_index, nxt_liquid_b_index) not in visited:
                nxt_characteristic = liquids[nxt_liqiud_a_index] + liquids[nxt_liquid_b_index]
                stack.append((nxt_liqiud_a_index, nxt_liquid_b_index, nxt_characteristic))
                visited.add((nxt_liqiud_a_index, nxt_liquid_b_index))

                if abs(nxt_characteristic) <= result[2]:
                    result = (nxt_liqiud_a_index, nxt_liquid_b_index, abs(nxt_characteristic))

print(liquids[result[0]], liquids[result[1]])