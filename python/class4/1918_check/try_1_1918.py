expression = input().strip()

operator_mul_di = ['*', '/']
operator_pl_mi = ['+', '-']

stack = []
buffer = []

buffer_check_num = 0

for char in expression:
    if char in operator_mul_di:
        stack.append(char)
        buffer_check_num += 1
    elif char in operator_pl_mi:
        stack.append(char)
    elif char == "(":
        buffer_check_num -= 1
    elif char == ")":
        buffer_check_num += 2
        if buffer_check_num == 1:
            while stack and buffer_check_num > 0:
                buffer.append(stack.pop())
                buffer_check_num -= 1
    else:
        buffer.append(char)
        if buffer_check_num == 1:
            while stack and buffer_check_num > 0:
                buffer.append(stack.pop())
                buffer_check_num -= 1

print(''.join(buffer), end="")
print(''.join(stack[::-1]), end="\n")