# 思想：归并排序
# 在排序过程中把逆序对的数目记录下来即可
# 方法是：前后的数组分别为nums1和nums2，若nums1中的元素大于nums2中的某个元素，则把nums1中剩余的元素个数加到count中
class Solution:
    def InversePairs(self, data):
        self.count = 0
        def merge_sort(nums):
            if len(nums) == 1:
                return nums
            nums1 = merge_sort(nums[:len(nums)//2])
            nums2 = merge_sort(nums[len(nums)//2:])
            i = j = 0
            temp = []
            while i < len(nums1) and j < len(nums2):
                if nums1[i] > nums2[j]:
                    temp.append(nums2[j])
                    j += 1
                    # count中增加的是：有多少个nums1中的元素>nums[j]
                    self.count += len(nums1) - i
                else:
                    temp.append(nums1[i])
                    i += 1
            if i < len(nums1):
                temp.extend(nums1[i:])
            if j < len(nums2):
                temp.extend(nums2[j:])
            return temp
        merge_sort(data)
        return self.count % 1000000007  # 题目要求
