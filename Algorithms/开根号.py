# 牛顿法：
# 构造f = x^2 - a = 0，利用泰勒公式一阶展开
# 求得公式为x = x_prev - f/f'
def sqrt_newton(num, threshold):
	prev, x = num/2, num
	while abs(prev - x) > threshold:
		prev = x
		x = (prev + num/prev)/2
	return x


# 二分法：
def sqrt_bisearch(num, threshold):
	if num < 0:
		return None
	elif num < 1:
		left, right = num, 1
	else:
		left, right = 0, num
	while abs(left-right) > threshold:
		mid = (left + right) / 2
		if mid ** 2 < num:
			left = mid
		elif mid ** 2 > num:
			right = mid
		else:
			return mid
	return mid

num = 0.25
threshold = 1e-5
print(sqrt_bisearch(num, threshold))
