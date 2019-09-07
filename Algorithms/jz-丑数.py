# 不能直接当作BFS来做，因为丑数中可能会有重复的现象
# 维持三个指针
class Solution:
    def GetUglyNumber_Solution(self, index):
        if not index:
            return 0
        result = [1] * index
        index_2 = index_3 = index_5 = 0
        for i in range(1, index):
            result[i] = min(result[index_2] * 2, result[index_3] * 3, result[index_5] * 5)
            if result[i] == result[index_2] * 2:
                index_2 += 1
            if result[i] == result[index_3] * 3:
                index_3 += 1 
            if result[i] == result[index_5] * 5:
                index_5 += 1
        return result[-1]
