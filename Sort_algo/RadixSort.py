def redix_sort(nums, digit):
	sorted_num = nums
	for i in range(digit):
		buckets = [[] for _ in range(10)]
		for num in sorted_num:
			buckets[num // (10**i) % 10].append(num)
		sorted_num = [n for l in buckets for n in l]
	return sorted_num

nums = [9, 1, 34, 2, 24, 15, 3, 0]
digit = 2  # 代表数字的最大位数k
print(redix_sort(nums, digit))

# 基数排序
# 思想：首先把数组按照个位装进10个桶里，相当于第一次排序
# 然后在该排序基础上对十位进行二次排序，以此类推
# 时间：O（kn）；空间：O（w+n），w为基数10
# 当数据量很大的时候基数排序要比快排好，且它是稳定排序，但是k也可能很大
