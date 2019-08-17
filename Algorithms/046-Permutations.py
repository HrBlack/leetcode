# 维护一个temp数组，在现有的序列基础上，将当前的num依次插入进去
# 时间：O(n*n!)；空间：O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = [[]]
        for num in nums:
			temp = []
            for item in result:
                for l in range(len(item)+1):  # 插入至0-n的任意位置
                    temp.append(item[:l] + [num] + item[l:])
            result = temp
        return result


# 递归解
# for xx in xxx or xxxx:注意这个用法，如果xxx是空的话，那么xx就被赋为xxxx中的元素（xxxx是个可迭代对象）
# 此处这个用法是为了防止当nums只有一个元素的情况
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[num] + item for i, num in enumerate(nums) for item in self.permute(nums[:i] + nums[i+1:]) or [[]]]
