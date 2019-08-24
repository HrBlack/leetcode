# 位运算
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        def index_digit(index, value):
            value = value >> index
            return value
        a = b = 0
        xor = index = 0
        for i in array:
            xor ^= i  # xor是两个数字ab的异或，即两者间不同的bit
        # 得到xor中bit是1的最右边的位置，并以此将数组分为两组
        while not (xor & 1):
            xor >>= 1
            index += 1
        for j in array:
            if index_digit(index, j) & 1:
                a ^= j
            else:
                b ^= j
        return [a, b]
