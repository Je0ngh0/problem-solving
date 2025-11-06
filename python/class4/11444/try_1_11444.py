import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

dp = [0,
 1,
 1,
 2,
 3,
 5,
 8,
 13,
 21,
 34,
 55,
 89,
 144,
 233,
 377,
 610,
 987,
 1597,
 2584,
 4181,
 6765,
 10946,
 17711,
 28657,
 46368,
 75025,
 121393,
 196418,
 317811,
 514229,
 832040,
 1346269,
 2178309,
 3524578,
 5702887,
 9227465,
 14930352,
 24157817,
 39088169,
 63245986,
 102334155,
 165580141,
 267914296,
 433494437,
 701408733,
 ]

divider = 1000000007

if n <= 44:
    result = dp[n]
else:
    my_sum = 0
    stack = [n]

    while stack:
        my_num = stack.pop()
        n1 = my_num // 2
        n2 = my_num - n1

        if n1 <= 44:
            my_sum += dp[n1]
        else:
            stack.append(n1)

        if n2 <= 44:
            my_sum += dp[n2]
        else:
            stack.append(n2)

    result = my_sum % divider

try:
    print(str(my_sum)+ "\n\n")
except:
    pass

print(str(result))