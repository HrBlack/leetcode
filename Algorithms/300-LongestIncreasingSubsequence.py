# DP:
# O（nlogn）解法，dp数组中存的是一个有序数列[2, 4, 8, ... , 0]，最后一位是0
# dp[i]中存的是长度为i+1的可能递增序列中最后一项的最小值
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        index = 0
        for i in range(len(nums)):
            left, right = 0, index
            while left < right:
                mid = (left + right) // 2
                if nums[i] < dp[mid]:
                    right = mid  # 之所以不能-1是因为nums[i]要替换的永远是dp中大于它的值
                elif nums[i] > dp[mid]:
                    left = mid + 1
                else:  # 如果nums[i]在dp里，那么直接break
                    right = mid
                    break
            dp[right] = nums[i]
            index = max(index, right + 1)  # 只有right=index时，即在最右边插入时index才+1
        return index

# 此题也可以利用两个for循环做，即O（n^2）解法
