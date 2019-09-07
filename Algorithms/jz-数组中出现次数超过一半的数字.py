# 时间O（n），空间：O（1）
# 如果用hashmap的话，空间将会是O（n）
class Solution:
    def MoreThanHalfNum_Solution(self, nums):
        count = 0
        for i in range(len(nums)):
            if count == 0:
                result = nums[i]
            if result == nums[i]:
                count += 1
            else:
                count -= 1
        count = 0
        # 确定该nums值是出现了一半以上
		for i in range(len(nums)):
            if nums[i] == result:
                count += 1
        if 2 * count > len(nums):
            return result
        return 0
