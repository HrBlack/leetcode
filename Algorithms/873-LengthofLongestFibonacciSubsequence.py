# DP
# 注意：题目里讲明了是Fibonacci-like subsequence，也就是说不是严格的斐波那契数列
# 只要满足x_n = x_n-1 + x_n-2的都是fibonacci-like subsequence
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        memo = set(A)
        dp = {}
		# 注意：是判断j-i是否在memo里，而不是判断j+i
        for j in range(len(A)):
            for i in range(j):
			    # A[j] - A[i] < A[i]的作用是保证子序列是递增的（10，4，14，18的情况）
                if A[j] - A[i] < A[i] and A[j] - A[i] in memo:
                    dp[(A[i], A[j])] = 1 + dp.get((A[j]-A[i], A[i]), 2)
        return max(dp.values() or [0])  # max里面不可以接空集
