# 思想：若n=4，则共有4 * 3!种组合，若k=14，则14=2*6 + 2，也就是说第一个数字应该是3，以此类推
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * n
        nums = list(range(1, n+1))
        result = ''
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i
        k -= 1
        for j in range(n-1, -1, -1):
            remainder = k // factorial[j]
            result += str(nums[remainder])
            k %= factorial[j]
            nums.remove(nums[remainder])
        return result 
