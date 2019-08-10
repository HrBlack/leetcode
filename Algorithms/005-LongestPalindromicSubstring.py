class Solution:
    def longestPalindrome(self, s: str) -> str:
        def compare(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]    
        
        substring = ''
        for index in range(len(s)):
            res_1 = compare(index, index)
            res_2 = compare(index, index+1)
            if len(res_1) > len(substring):
                substring = res_1
            if len(res_2) > len(substring):
                substring = res_2
        return substring
        
# 构建一个compare函数，函数设计很重要，输入是i，j两个坐标，输出是数组序列
# 在每个index下都要比较两次，即单数还是双数的问题
