# 题目和046的区别就在于要防止重复
# 防止重复的关键就在if语句那里
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_res = []
            for item in result:
                for i in range(len(item)+1):  # 可以插在0-n的任意位置
                    new_res.append(item[:i] + [num] + item[i:])
                    if i < len(item) and item[i] == num: # 如果原item中已经有num，这时只插入一次即可
                        break
            result = new_res
        return result
