def bubble_sort(nums):
	length = len(nums)
	while length > 1:
		for i in range(1, length):
			if nums[i-1] > nums[i]:
				nums[i-1], nums[i] = nums[i], nums[i-1]
		length -= 1

nums = [9, 1, 3, 4, 2, 8, 5, 7, 6, 0]
bubble_sort(nums)
print(nums)

# 冒泡排序
# 时间：n^2；空间：O（1）
# 通过控制length，来让数组中最右边的数字不再变化
# 思想：从左向右依次两两比较，把最大的数字放在最右边
