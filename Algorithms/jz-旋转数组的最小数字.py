# 题目：
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# 给出的所有元素都大于0，若数组大小为0，请返回0。

# 思路：二分查找，维持两个指针，找到左侧递增数组的最后一个元素与右侧递增数组的第一个元素即可
class Solution:
    def minNumberInRotateArray(self, array):
        if not array:
            return 0
        left, right = 0, len(array) - 1
        while left < right:
            mid = (left+right)//2
            if array[mid] > array[right]:  # 目标值一定在mid右侧
                left = mid + 1
            elif array[mid] < array[right]:  # mid右侧单调递增
                right = mid  # 正常二分时是可以-1的，但是这里mid本身就有可能是目标值，如果-1就会漏掉它
            else:
                # 当递增数列中有元素相同时：[0, 1, 1, 1, 3]
                right -= 1
        return array[right]
