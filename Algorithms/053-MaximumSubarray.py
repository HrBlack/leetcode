# DP：
# 看似简单，不可掉以轻心
# dp中存的是当前时刻所能得到的最大值，可见其未必是最优解，所以要及时更新result
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = dp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= 0:
                dp = nums[i] if dp < 0 else nums[i] + dp
            else:
                dp = max(0, dp) + nums[i]
            result = max(result, dp)
        return result
