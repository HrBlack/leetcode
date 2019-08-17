# 统计一个数字在排序数组中出现的次数
# 思想：找到k+0.5和k-0.5在数组中的位置，相减即可
class Solution:
    def GetNumberOfK(self, data, k):
        def BiSearch(k):
            i, j = 0, len(data) - 1
            while i <= j:
                mid = (i + j)//2
                if data[mid] > k:
                    j = mid - 1
                elif data[mid] < k:
                    i = mid + 1
            return i
        return BiSearch(k+0.5) - BiSearch(k-0.5)
