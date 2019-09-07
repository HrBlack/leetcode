# 思想：先用mid来判断下左边或右边是否是升序的，右边的条件是唯一的，所以先判断target是否在右侧
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                if target > nums[mid] or target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
		# 注意这里的结果是left，不是mid
        if len(nums) >= 1 and nums[left] == target:
            return left
        return -1
