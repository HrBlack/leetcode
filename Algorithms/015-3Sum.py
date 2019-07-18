# 两种方法的复杂度都是O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 把3Sum转化成two sum问题
        result = []
        nums.sort()  # 需要先按位排序
        def two_sum(sub_nums, target):
            memo, i = {}, -1
            while i < len(sub_nums):
				i += 1
                if target-sub_nums[i] in memo.keys():
                    result.append([-target, target-sub_nums[i], sub_nums[i]])
                else:
                    memo[sub_nums[i]] = 1
                    continue  # 这里的continue必不可少，[0,0,0]的情况
				# 这里注意，在一个while循环里就把该item的所有重复都滤掉
				# 不要忘了i的左右边界
                while 0 < i < len(sub_nums) and sub_nums[i] == sub_nums[i-1]:
                    i += 1

        for j, num in enumerate(nums):
			# 第二个防止重复的地方
			# 注意，我们需要在当前位置“回头看”
            if j >= 1 and num == nums[j-1]:
                continue
            two_sum(nums[j+1:], -num)
        return result

# 方法二：三指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
		# 此题不要写成target = -num的形式，麻烦 
        result = []
        nums.sort()
        for i, num in enumerate(nums):
			# 第一个防重复的地方
            if i >= 1 and num == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[left] + nums[right] + nums[i]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
					# 第二个防重复的地方
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    while right > left and nums[left] == nums[left+1]:
                        left += 1
                    right -= 1; left += 1
            
        return result
