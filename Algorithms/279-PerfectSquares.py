class Solution:
    def numSquares(self, n: int) -> int:
        # BFS
        # 逐层遍历，target与tmp的切换很有意思
        # 注意：set里面要接受可以迭代的对象，但写成{}可以直接收int
        i = 1
        while i*i <= n:  # 必须要有等号！
            i += 1
        nums = [num*num for num in range(1, i)]
        level = {n}  # 记录第k层的所有diff差值
        count = 0
        while level:
            memo = set()
            for t in level:
                for i in nums:
                    if i == t:
                        return count + 1
                    if i > t:
                        break
                    memo.add(t - i)
            level = memo
            count += 1
        return count 


class Solution:
    def numSquares(self, n: int) -> int:
        # DP
		# 从前向后遍历，但DP在这种问题中并不管用，因为nums里的元素跨度很大
        i = 1
        while i*i <= n:
            i += 1
        nums = [num*num for num in range(1, i)]
        memo = [float("+inf") for _ in range(n+1)]
        memo[0] = 0
        for target in range(1, n+1):
            memo[target] = min(memo[target-num] for num in nums if num <= target) + 1
        return memo[-1]
