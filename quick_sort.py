def quick_sort(lst, left, right):
	if left >= right:
		return

	pivot = lst[(left + right)//2]
	index = partition(lst, left, right, pivot)
	quick_sort(lst, left, index-1)
	quick_sort(lst, index, right)
	
# quick_sort is dependant on partition
def partition(lst, left, right, pivot):
	while left <= right:
		while lst[left] < pivot:
			left += 1

		while lst[right] > pivot:
			right -= 1

		if left <= right:
			lst[left], lst[right] = lst[right], lst[left]
			left+=1
			right-=1

	return left
