# DP
# 注意两件事：1. dp[1]的初值设置 2. max(j, dp[j])
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 2:
            return 0
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], max(i-j, dp[i-j]) * max(j, dp[j]))
        return dp[-1]
