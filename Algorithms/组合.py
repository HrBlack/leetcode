def combination(letters, k):
	result = []
	if k == 0:
		return ['']
	for i in range(len(letters)):
		for letter in combination(letters[i+1:], k-1):
			result.append(letters[i] + letter)
	return result

letters = 'abcd'
k = 2
print(combination(letters, k))
