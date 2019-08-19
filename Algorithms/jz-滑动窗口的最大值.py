# 思想：利用双向队列（list即可）来存储窗口
# 队列正常是从右侧进，从左侧出；最左侧存储的是最大值，每个新元素从右进来，把窗口中剩余的小于它的元素pop掉
# 暴搜复杂度是O（nk），这样做可以介于O（n）与O（nk）之间
class Solution:
    def maxInWindows(self, nums, size):
        # queue里存储的是index
        queue, result = [], []
        for i in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            if queue and i - queue[0] + 1 > size:  # 最大值已经不在该窗口里了
                queue.pop(0)
            queue.append(i)
            if size and i+1 >= size:
                result.append(nums[queue[0]])
        return result
