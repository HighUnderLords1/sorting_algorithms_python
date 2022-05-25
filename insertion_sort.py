def insertion_sort(lst):
	indexing_length = range(1, len(lst))
	for i in indexing_length:
		value_to_sort = lst[i]

		while lst[i-1] > value_to_sort and i > 0:
			lst[i], lst[i-1] = lst[i-1], lst[i]
			i -= 1

	return lst
