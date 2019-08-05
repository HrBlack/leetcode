# 方法一：DFS
# 比DP方法快很多
# 注意：这里采用了按位修改self.result，所以直接return意味着什么都没有修改
from math import ceil
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums = sorted(coins)
        self.result = float('+inf')
        
        def dfs(count, target, coins):
            if not coins:  # 硬币用没了
                return 
            if ceil(target / coins[-1]) + count >= self.result:  # 总count比当前结果大
                return
            if target % coins[-1] == 0:  # 此处很关键，不能写成if target == 0的形式，那样就相当于没利用coins[-1]
                self.result = count + target // coins[-1]
                return
            for i in range(target // coins[-1], -1, -1):
                dfs(count + i, target - i * coins[-1], coins[:-1])
            return 
        
        dfs(0, amount, nums)
		# 最后返回-1是题目要求
        return self.result if self.result != float('+inf') else -1

# 方法二：DP
# 注意：一定要让memo[0]初始化为0，另外memo的长度应为amount+1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo = [float('+inf') for _ in range(amount + 1)]
        memo[0] = 0
        for i in range(amount + 1):
            for num in coins:
                if i - num >= 0:
                    memo[i] = min(memo[i], 1 + memo[i-num])
        return memo[-1] if memo[-1] != float('+inf') else -1
