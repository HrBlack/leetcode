# 二进制相加
# 写法巧妙
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry, add = 0, 0
        i, j = len(a), len(b)
        while i > 0 or j > 0:
            add = carry
            i -= 1
            j -= 1
            if i >= 0:
                add += int(a[i])
            if j >= 0:
                add += int(b[j])
            carry = add // 2
            remainder = add % 2
            result = str(remainder) + result
        if carry != 0:
            result = str(carry) + result
        return result
