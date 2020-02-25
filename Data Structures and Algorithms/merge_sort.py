import numpy as np 
unsorted = np.random.randint(20, size=10)
print(unsorted)

def mergesort(numlist):
	numlist = list(numlist)
	if len(numlist) > 1:
		l, r = numlist[len(numlist)//2:], numlist[:len(numlist)//2]
		l = mergesort(l) # left section 
		r = mergesort(r) # right section
		i,j,k = 0,0,0 # index for left, right and whole section of the input array

		while i < len(l) and j < len(r):
			if l[i] <= r[j]:
				numlist[k] = l[i]
				i += 1
			else:
				numlist[k] = r[j]
				j += 1
			k += 1
		"""
		# add the remaining values of the left and right section 
		# of the merge sort
		"""
		while i < len(l):
			numlist[k] = l[i]
			i += 1
			k += 1
		while j < len(r):
			numlist[k] = r[j]
			j += 1
			k += 1

	return numlist


		
sorted_list = mergesort(unsorted)
print(sorted_list)