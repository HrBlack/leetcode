# 移动窗口（双指针）+ hash map方法
# 移动右边指针直到找到有效子串，然后移动左指针减小子串长度
from collections import Counter
# Counter是将list中的元素计数后加入dict中
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map = Counter(t)
        left = right = 0
        length = len(s) + 1
        counter = len(t)
        while right < len(s):
            if hash_map.get(s[right], 0) > 0:
                counter -= 1
            hash_map[s[right]] -= 1
            right += 1
            # 当counter=0时即为valid substring，移动左指针
            while counter == 0:
                if right - left < length:
                    start, length = left, right - left
                hash_map[s[left]] += 1
                if hash_map[s[left]] > 0:
                    counter += 1
                left += 1
        if length != len(s) + 1:
            return s[start: start+length]
        return ''
