class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 递归方法，不要忘记考虑n小于0的情况，注意如果用**2来做平方就会溢出
		# 不要想的太复杂
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.myPow(x, -n)
        else:
            half_pow = self.myPow(x, n//2)
            if n % 2 == 0:
                return  half_pow * half_pow
            else:
                return half_pow * half_pow * x
