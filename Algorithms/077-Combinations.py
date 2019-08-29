# DFS递归
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(res, nums):
            if len(res) == k:
                ans.append(res)
                return
            for i in range(len(nums)):
                dfs(res+[nums[i]], nums[i+1:])
            return
        for i in range(1, n+1):
            dfs([i], list(range(i+1, n+1)))
	return ans

# 栈
class Solution:
    def combine(self, n, k):
        ans, stack = [], []
        x = 1
        while True:
            if len(stack) == k:
                ans.append(stack[:])
            if len(stack) == k or x > n - k + len(stack) + 1:  # 这是关键，如果x大于该值，则后面的数字就不够了
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
