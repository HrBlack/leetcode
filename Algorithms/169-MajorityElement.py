# 这道题和jz-数组中出现次数超过一半的数字的区别是：它假设数组中一定存在majority数
# 这里的majority是指出现次数超过一半的数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = nums[0], 1
        for i, item in enumerate(nums[1:]):
            if count == 0:
                count = 1
                majority = item
            elif item == majority:
                count += 1
            else:
                count -= 1
        return majority
