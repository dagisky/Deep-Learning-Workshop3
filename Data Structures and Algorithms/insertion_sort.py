import numpy as np

unsorted = np.random.randint(20, size=10)
print(unsorted)

def insertion_sort(num_list):
	num_list = list(num_list)
	for i in range(1,len(num_list)):
		j = i
		while j>0 and num_list[j] < num_list[j-1]:
			temp = num_list[j]
			num_list[j] = num_list[j-1]
			num_list[j-1] = temp
			j -= 1
	return num_list

sorted_list = insertion_sort(unsorted)
print(sorted_list)