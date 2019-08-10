class Solution:
    def convert(self, s: str, numRows: int) -> str:
		# numRows=1的情况会让下面循环里的if报错
        if numRows <= 1: 
            return s
        memo = ['' for _ in range(numRows)]
        j = 0
        for i in range(len(s)):
            memo[j] += s[i]
            if j == 0:
                step = 1
            if j == numRows - 1:
                step = -1
            j += step
        return ''.join(memo)

# 维护一个memo数组，数组中每个元素都代表zigzag的一行
# 巧妙的是step的构建，无论是向上还是向下都共用这个step
