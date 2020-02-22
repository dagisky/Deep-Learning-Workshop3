import numpy as np

unsorted = np.random.randint(20, size=10)
print(unsorted)

def selection_sort(num_list):
	num_list = list(num_list)
	for i in range(len(num_list)):
		minimum = num_list[i]
		for j in range(i+1, len(num_list)):
			if num_list[j] < minimum:
				minimum = num_list[j]
				num_list[j] = num_list[i]
				num_list[i] = minimum
	return num_list

sorted_list = selection_sort(unsorted)
print(sorted_list)
