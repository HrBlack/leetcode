class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 注意！此题是DP算法，不要上来想简单了直接用for
        max_length, curr_length = 0, 0
        last_repetition_index = 0  # 记录最近的产生重复的坐标
        memo = {}
        for i, item in enumerate(s):
            if item not in memo.keys():
                memo[item] = i
                curr_length += 1
            else:
                max_length = max(max_length, curr_length)
                # 更新左侧的坐标
                last_repetition_index = max(memo[item], last_repetition_index)
                curr_length = i - last_repetition_index
                # 一定要记得更新item的位置
                memo[item] = i
        # 如果从来没有重复的情况，更新max
        max_length = max(max_length, curr_length)
        return max_length
