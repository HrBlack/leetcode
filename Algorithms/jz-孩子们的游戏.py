# 约瑟夫环的问题：
# 若第一次0～n-1的序列中被拿走的是k，那么接下来就是从k+1一直遍历到n-1，再从0到k-1
# 此时我们将k+1作为新序列的起点，即坐标为0；将新坐标转化为老坐标的公式为x' = (x+m) % n
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0:
            return -1
        dp = 0  # 代表n=1的情况
        for i in range(2, n+1):
            dp = (dp + m) % i
        return dp
