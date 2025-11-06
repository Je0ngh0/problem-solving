expression = input().strip()

operator_mul_di = ['*', '/']
operator_pl_mi = ['+', '-']
parenthesis = ['(', ')']

stack = []
buffer = []

l_o = 0
parenthesis_num = 0

for char in expression:
    if char in operator_mul_di:
        c_o = 0 + parenthesis_num
    elif char in operator_pl_mi:
        c_o = 1 + parenthesis_num
    elif char == "(":
        parenthesis_num -= 2
        continue
    elif char == ")":
        parenthesis_num += 2
        continue
    else:
        buffer.append(char)
        continue

    while l_o <= c_o:
        if stack:
            l_char, l_o = stack.pop()
            buffer.append(l_char)
        else:
            break

    stack.append((char, l_o))
    l_o = c_o

while stack:
    buffer.append(stack.pop()[0])

print(''.join(buffer), end="")