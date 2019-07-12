import random

def sample(nums, k):
	result = nums[:k]
	for i in range(k, len(nums)):
		index = random.randint(0, i)
		if index < k:
			result[index] = nums[i]
	return result


if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	k = 5
	print(sample(nums, 5))
	
