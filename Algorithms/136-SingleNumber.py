# 异或即可
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        init = 0
        for item in nums:
            init = init ^ item
        return init
