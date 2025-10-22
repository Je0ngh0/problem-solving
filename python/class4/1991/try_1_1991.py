import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = [input().strip().split() for _ in range(n)]

graph = dict()
for root, right, left in arr:
    graph[root] = [right, left]


def travel(graph: dict, start: str, visited: set, result: dict):
    root_val = start
    left_val = graph[start][0]
    right_val = graph[start][1]

    left_pre, right_pre = [[], []]
    left_inorder, right_inorder = [[], []]
    left_post, right_post = [[], []]

    if left_val != '.':
        travel(graph, left_val, visited, result)
        left_pre = result["pre"]
        left_inorder = result["inorder"]
        left_post = result["post"]
    if right_val != '.':
        travel(graph, right_val, visited, result)
        right_pre = result["pre"]
        right_inorder = result["inorder"]
        right_post = result["post"]

    result["pre"] = [root_val] + left_pre + right_pre
    result["inorder"] = left_inorder + [root_val] + right_inorder
    result["post"] = left_post + right_post + [root_val]

start = 'A'
visited = {start}
result = dict()
travel(graph, start, visited, result)

for value in result.values():
    print(f"{"".join(value)}\n")