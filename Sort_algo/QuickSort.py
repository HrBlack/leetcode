def quick_sort(nums, i, j):
	if i >= j:
		return
	pivot = nums[i]
	left, right = i, j
	while left < right:
		while left < right and nums[right] > pivot:
			right -= 1
		if left < right:
			nums[left] = nums[right]
			left += 1  # 注意这个地方，不能忘	
		while left < right and nums[left] < pivot:
			left += 1
		if left < right:
			nums[right] = nums[left]
			right -= 1
	nums[left] = pivot
	
	quick_sort(nums, i, left-1)
	quick_sort(nums, left+1, j)

nums = [9, 1, 2, 4, 3, 7, 6, 8, 0, 5]
quick_sort(nums, 0, len(nums)-1)
print(nums)


# 递归快排
# 时间：nlogn；空间：logn（每一层仍然是O（1），但是有递归深度）
