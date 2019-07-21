def shell_sort(nums):
	length = len(nums)
	gap = length//2
	while gap >= 1:
		# insert sort
		for i in range(gap, length):
			for j in range(i-gap, -1, -gap):
				if nums[j+gap] < nums[j]:
					nums[j+gap], nums[j] = nums[j], nums[j+gap]
				else:
					break
		gap //= 2

nums = [9, 1, 2, 5, 3, 4, 7, 6, 8, 0]
shell_sort(nums)
print(nums)

# 希尔排序
# 时间：n^1.3，即介于n与n^2之间；空间：O（1）
# 相当于带有跳跃（gap）的直接插入排序
