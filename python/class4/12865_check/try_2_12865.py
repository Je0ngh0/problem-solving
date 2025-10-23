# 평범한 배낭 (BOJ 12865)

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]  # (W, V)

# dp[i] = 무게 i일 때 가질 수 있는 최대 가치
dp = [0] * (K + 1)

for w, v in items:
    # 뒤에서부터 갱신해야 중복 사용이 안 됨 (0/1 배낭)
    for i in range(K, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[K])
