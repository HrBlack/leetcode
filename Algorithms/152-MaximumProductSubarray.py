# DP
# 思路：连续乘积最大值要么是前一时刻的最大值*当前值，要么就是当前值本身
# 维护最大值与最小值，若当前值为负则两者对换；注意要及时将result更新
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = large = small = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= 0:
                large, small = small, large
            large = max(nums[i], large * nums[i])
            small = min(nums[i], small * nums[i])
            result = max(large, result)
        return result
