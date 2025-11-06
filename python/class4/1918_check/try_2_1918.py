expression = input().strip()

operator_mul_di = ['*', '/']
operator_pl_mi = ['+', '-']
parenthesis = ['(', ')']

stack = []
buffer = []
l_n = 4

for i, char in enumerate(expression):
    if char == '(':
        l_n = 4
        continue
    elif char in operator_mul_di:
        c_n = 1
    elif char in operator_pl_mi:
        c_n = 2
    elif char == ')':
        l_n = 0
        continue
    else:
        buffer.append(char)
        continue

    while l_n <= c_n:
        if stack:
            l_char, l_n = stack.pop()
            buffer.append(l_char)

    if c_n < l_n:
        stack.append((char, l_n))
        l_n = c_n


while stack:
    buffer.append(stack.pop()[0])


print(''.join(buffer), end="")