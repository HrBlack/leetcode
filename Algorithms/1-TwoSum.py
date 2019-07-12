class Solution:
	# 遍历数组，如果差值diff不在memo里，那就把该值item存进memo
	# 看似简单，逻辑要对得上，不能将diff存进去
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, item in enumerate(nums):
            diff = target - item
            if diff not in memo.keys():
                memo[item] = i
            else:
                return [memo[diff], i]
        return []
            
        
