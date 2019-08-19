class Solution:
    def StrToInt(self, s):
        s = s.strip()
        if not s or not (s[0].isdigit() or s[0] in {'-', '+'}):
            return 0
        index, sign = 0, 1
        res = 0
        if s[0] in {'-', '+'}:
            sign = -1 if s[0] == '-' else 1
            index = 1
        for item in s[index:]:
            if not item.isdigit():
                return 0
            res *= 10
            res += int(item)
        res *= sign
        return max(min(res, 2**31-1), -2**31)
