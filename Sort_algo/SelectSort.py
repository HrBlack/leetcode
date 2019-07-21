def select_sort(nums):
	for i in range(0, len(nums)):
		minimum = nums[i]
		memo = i
		for j in range(i+1, len(nums)):
			if nums[j] < minimum:
				minimum = nums[j]
				memo = j
		nums[i], nums[memo] = minimum, nums[i]

nums = [9, 1, 2, 5, 4, 3, 8, 6, 7, 0]
select_sort(nums)
print(nums)


# 简单/直接选择排序
# 思想：在一段序列中找到最小的值，把它同当前序列的第一个元素对换
# 时间：n^2；空间：O（1）
