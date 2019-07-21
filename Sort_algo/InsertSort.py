def insert_sort(nums):
	for i in range(1, len(nums)):
		for j in range(i-1, -1, -1):
			# 注意：是j+1同j比较，和i没有关系
			if nums[j+1] < nums[j]:
				nums[j+1], nums[j] = nums[j], nums[j+1]
			else:
				break
	return nums

nums = [9, 1, 2, 5, 7, 4, 8, 6, 3, 0, 5]
print(insert_sort(nums))

# 直接插入排序
# 时间：n^2; 空间：O（1）
# 思想：像插入扑克牌一样，拿到num后和前面的序列依次比较
# 注意：和冒泡排序的差别，插入排序后暂时得到的有序序列并不是最后的成品,
# 后面很有可能还有新的元素插在前面，但是冒泡排序排好的部分就不再变化了;
# 这里交换的部分完全也可以由插入代替，但是数组整体移动复杂度会增大
