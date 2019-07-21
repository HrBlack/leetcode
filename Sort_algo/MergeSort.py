def merge_sort(nums):
	if len(nums) == 1:
		return nums
	a = merge_sort(nums[:len(nums)//2])
	b = merge_sort(nums[len(nums)//2:])
	sorted_list, i, j = [], 0, 0
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			sorted_list.append(a[i])
			i += 1
		else:
			sorted_list.append(b[j])
			j += 1
	sorted_list.extend(b[j:])
	sorted_list.extend(a[i:])
	return sorted_list

nums = [9, 1, 3, 2, 5, 8, 7, 0, 6, 4]
print(merge_sort(nums))

# 归并排序：分治法
# 思想：把数组递归分为两份，直到只剩下一个元素
# 然后再两两合并
# 时间：nlogn；空间：O（n），因为虽然每次都用了和待排序数组相同的辅助表，
# 但每轮递归后都会释放掉该表，所以最多只占用n的空间（快排叠加是因为没释放，下一轮要用）
