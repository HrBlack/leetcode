# 方法一：
# DP:从后向前遍历
# 时间=空间=O（n^2）
# memo[i][j]表示word1[i:]与word2[j:]匹配需要的最短距离，包括i与j
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for i in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            memo[i][-1] = len(word1) - i
        for j in range(len(word2)+1):
            memo[-1][j] = len(word2) - j
        for r in range(len(word1)-1, -1, -1):
            for c in range(len(word2)-1, -1, -1):
                if word1[r] == word2[c]:
                    memo[r][c] = memo[r+1][c+1]
                else:
                    memo[r][c] = 1 + min(memo[r+1][c], memo[r][c+1], memo[r+1][c+1])
        return memo[0][0]

# 方法二：
# 利用O（n）空间复杂度，从前向后遍历
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [i for i in range(len(word2)+1)]  # memo里初值是为了防止word1为空
        for r in range(1, len(word1)+1):
            prev, memo[0] = r - 1, r  # 因为prev代表左上，所以它要-1
            for c in range(1, len(word2)+1):
                temp = memo[c]
                if word1[r-1] == word2[c-1]:
                    memo[c] = prev
                else:
                    memo[c] = 1 + min(memo[c-1], memo[c], prev)  # memo[c-1]代表左，memo[c]代表下，prev代表左上角
                prev = temp
        return memo[-1]
