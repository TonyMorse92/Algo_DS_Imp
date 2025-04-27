# Basic quicksort check


def quick_sort_nums(lst):
	if (len(lst) < 2):
		return lst

	pvt = lst[len(lst) // 2]

	left = [num for num in lst if num < pvt]

	mid = [num for num in lst if num == pvt]

	right = [num for num in lst if num > pvt]

	return quick_sort_nums(left) + mid + quick_sort_nums(right)



