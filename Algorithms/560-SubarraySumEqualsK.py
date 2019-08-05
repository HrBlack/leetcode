# 题目要求返回有多少个sum=K的
# 遍历数组，利用dict存储已有的前缀和，若此刻的前缀和-k出现在了dict里，则结果+1
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {0: 1}  # 当sums-k=0时，默认+1
        sums = res = 0
        for num in nums:
            sums += num
            if sums - k in memo.keys():
                res += memo[sums-k]
            memo[sums] = memo.get(sums, 0) + 1
        return res
