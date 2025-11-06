import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
n = n-1

queue = [n]
result = []

while True:
    x = queue.pop()
    if x <= 1:
        break
    if x % 2 == 0:
        result.append((x//2, 0))
    else:
        result.append((x//2, 1))
    
    queue.append(x//2)
    if x//2 == 1:
        break

divider = 1000000007
def multiply_matrices(mat_a: list[list[int]], mat_b: list[list[int]]) -> list[list[int]]:
    product = [
        [(mat_a[0][0]*mat_b[0][0] + mat_a[0][1]*mat_b[1][0]) % divider, (mat_a[0][0]*mat_b[0][1] + mat_a[0][1]*mat_b[1][1]) % divider],
        [(mat_a[1][0]*mat_b[0][0] + mat_a[1][1]*mat_b[1][0]) % divider, (mat_a[1][0]*mat_b[0][1] + mat_a[1][1]*mat_b[1][1]) % divider]
    ]

    return product

def apply_matrix_to_vector(matrix: list[list[int]]) -> int:
    vector = [
        [1],
        [0]
    ]
    result = [
        [matrix[0][0]*vector[0][0] + matrix[0][1]*vector[1][0]],
        [matrix[1][0]*vector[0][0] + matrix[1][1]*vector[1][0]],
    ]

    return result

init_matrix = [
    [1, 1],
    [1, 0]
]
matrix = init_matrix.copy()

for _, add_one in result[::-1]:
    if add_one:
        matrix = multiply_matrices(multiply_matrices(matrix, matrix), init_matrix)
    else:
        matrix = multiply_matrices(matrix, matrix)

print(f"{apply_matrix_to_vector(matrix)[0][0] % divider}\n")