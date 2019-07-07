class Solution:
    def numSquares(self, n: int) -> int:
        # BFS
		# 逐层遍历，target与tmp的切换很有意思
		# 注意：set里面要接受可以迭代的对象，但写成{}可以直接收int
		i = 1
        while i*i <= n:
            i += 1
        nums = [num*num for num in range(1, i)]
        target = {n}
        count = 0
        while target:
            tmp = set()
            for t in target:
                for i in nums:
                    if i == t:
                        return count+1
                    if i > t:
                        break
                    tmp.add(t - i)
            target = tmp
            count += 1
        return count 
