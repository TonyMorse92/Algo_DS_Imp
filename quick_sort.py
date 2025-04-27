# Basic quicksort check
import Data.gen_data as gen

def quick_sort_nums(lst):
	if (len(lst) < 2):
		return lst

	pvt = lst[len(lst) // 2]

	left = [num for num in lst if num < pvt]

	mid = [num for num in lst if num == pvt]

	right = [num for num in lst if num > pvt]

	return quick_sort_nums(left) + mid + quick_sort_nums(right)


example = gen.gen_ints(size=10)

print(example)

example = quick_sort_nums(example)

# Convert numpy types back to python
example = [num.item() for num in example]

print(example)
