def merge_sort(lst):
	if len(lst) == 1:
		return lst

	middle = len(lst)//2
	left = lst[0 : middle]
	right = lst[middle: len(lst)]

	return merge(merge_sort(left), merge_sort(right))

# merge_sort is dependent on merge
def merge(left, right):
	result = []
	indexLeft = 0
	indexRight = 0

	while indexLeft < len(left) and indexRight < len(right):
		if left[indexLeft] < right[indexRight]:
			result.append(left[indexLeft])
			indexLeft+=1
		else:
			result.append(right[indexRight])
			indexRight+=1

	return result+left[indexLeft:len(left)]+right[indexRight:len(right)]
