# 将int转化为str
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        string = str(x)
        i = 0
        while i <= len(string) // 2:
            if string[i] == string[len(string)-1-i]:
                i += 1
                continue
            return False
        return True

# 不转化
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        temp = 0
        while temp < x:
            temp = temp * 10 + x % 10  # 右半部分
            x //= 10  # 左半部分
        return x == temp or x == temp//10  # 分别代表x位数为偶数或奇数
