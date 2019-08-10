class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] in ['+', '-']:
            s = s[0] + s[1:][::-1]
        else:
            s = s[::-1]
        return int(s) if 2**31 >= int(s) >= -2**31 else 0


# 题目要求如果溢出的话，则返回0
