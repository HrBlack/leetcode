# 注意题目要求返回的是整数，所以只要x在mid和mid+1之间就可以了
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x  # right不能是x/2，会有x=1的情况
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return mid
