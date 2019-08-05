def heap_sort(nums):
	def sift(i, length):
		while i < length:
			if 2*i+2 >= length or nums[2*i+1] < nums[2*i+2]:
				small = 2 * i + 1
			else:
				small = 2 * i + 2
			if small < length and nums[small] < nums[i]:
				nums[small], nums[i] = nums[i], nums[small]
			else:
				break
			i = small
	
	res = []
	length = len(nums)
	# 建堆：O(n)
	# n/2个节点，倒数第二层下溯1次，倒数第三层下溯2次，以此类推
	# 有证明，这样最后会收敛到O(n)
	for i in range(length//2, -1, -1):
		sift(i, length)
	# 维护堆：O(nlogn)
	for i in range(length):
		# 把最小值都存在了nums后面
		# 此步复杂度nlogn：n个点，每个点最多要向下走logn层
		nums[0], nums[length-i-1] = nums[length-i-1], nums[0]
		sift(0,length-i-1)
	return nums

nums = [9, 1, 7, 3, 6, 4, 8, 2, 0, 5]
print(heap_sort(nums))

# 空间复杂度：O(1)，按位修改；时间复杂度：O(nlogn)
# 注意，建了最小堆，但是把最小的值放在了nums后面，所以最后是一个由大到小的排序
