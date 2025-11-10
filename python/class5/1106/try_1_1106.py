import sys

input = sys.stdin.readline
print = sys.stdout.write

C, N = map(int, input().strip().split())
arr = [tuple(map(int, input().strip().split())) for _ in range(N)]

sorted_arr = sorted(arr, key = lambda x: x[1] / x[0], reverse = True)

remain = C
tot_cost = 0
exceed_cost = float("inf")

for cost, customer in sorted_arr:
    invest_num = remain // customer
    
    remain -= invest_num * customer
    

    if remain == 0:
        if exceed_cost <= invest_num * cost:
            tot_cost += exceed_cost
        break
    else:
        if exceed_cost <= (invest_num + 1) * cost:
            pass
        else:
            tot_cost += invest_num * cost
            exceed_cost = cost

print(str(tot_cost + exceed_cost))