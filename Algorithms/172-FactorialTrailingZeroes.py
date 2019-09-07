# 数学题：0仅可能是又2*5构成，因为2比5多，那么就只看有多少个因子5即可
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n//5)
