class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = len(nums) - 1
        while left >= 1 and nums[left-1] >= nums[left]:
            left -= 1
        if left == 0:
            nums.reverse()
            return
        right = left
        while right < len(nums) and nums[right] > nums[left-1]:
            right += 1
        nums[right-1], nums[left-1] = nums[left-1], nums[right-1]
        right = len(nums) - 1
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1
        return
