# 堆排序的思想
# 时间：O（nlogk）
class Solution:
    def findKthLargest(self, array: List[int], k: int) -> int:
        nums = array[:k]
        def heap_sort(i):
            while 2 * i + 1 < len(nums):
                if 2 * i + 2 >= len(nums) or nums[2*i+1] < nums[2*i+2]:
                    small = 2 * i + 1
                else:
                    small = 2 * i + 2
                if nums[small] < nums[i]:
                    nums[small], nums[i] = nums[i], nums[small]
                i = small
        for j in range(k-1, -1, -1):
            heap_sort(j)
        for i in range(k, len(array), 1):
            if array[i] <= nums[0]:
                continue
            nums[0] = array[i]
            heap_sort(0)
        return nums[0]

# 快排思想：最快是O（n），最慢是O（n*n）
class Solution:
    def findKthLargest(self, array: List[int], k: int) -> int:
        # 注意这种新的写法比较巧妙，最后返回的应该是right
        def partition(i, j):
            if i == j:
                return i
            pivot = array[i]
            left, right = i + 1, j
            while left <= right:  # 注意是小于等于
                if array[right] < pivot and array[left] > pivot:
                    array[right], array[left] = array[left], array[right]
                    right -= 1
                    left += 1
                if array[right] >= pivot:
                    right -= 1
                if array[left] <= pivot:
                    left += 1
            array[i], array[right] = array[right], array[i]
            return right

        left, right = 0, len(array) - 1
        while True:
            index = partition(left, right)
            if len(array) - index < k:
                right = index - 1
            elif len(array) - index > k:
                left = index + 1
            else:
                return array[index]
