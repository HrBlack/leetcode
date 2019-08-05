# 方法一：逐个字符比较
class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        min_length = min([len(item) for item in strs or ['']])  # 表示的是最小的长度
        i, res = 0, ''
        while i < min_length:
            letter = strs[0][i]
            for s in strs:
                if s[i] == letter:
                    continue
                else:
                    return res
            res += letter
            i += 1
        return res

# 方法二：只比较最大与最小的两个字符串
# 对字符取min或max指的是数值上的大小，即'ad' > 'abcd'
class Solution:
    def longestCommonPrefix(self, m):
        if not m:
            return ''
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            if i < len(s2) and c != s2[i]:
                return s1[:i]
        return s1
