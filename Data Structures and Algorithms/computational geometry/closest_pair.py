import numpy as np 
import math
pts = np.random.randint(20, size=(10,2))
print(pts)

def Euclidean_Distance(a, b):
	return math.sqrt(a**2+b**2)


def BruteForceClosestPair(Array):
	# this algorithm opreates at O(n^2)
    size = len(Array)
    minimum_distance = Euclidean_Distance(Array[0],Array[1])
    Target_Pair = (Array[0],Array[1])
    if len(Array) == 2:
        return Euclidean_Distance(Array[0],Array[1]),Array[0],Array[1]
    for i in range(0,size):
        for j in range(i+1,size):
            distance = Euclidean_Distance(Array[i],Array[j])
            if distance < minimum_distance:
                minimum_distance = distance
                Target_Pair = (Array[i],Array[j])
    return minimum_distance,Target_Pair


def mergesort(numlist, sorting='x'):
	numlist = list(numlist)
	if len(numlist) > 1:
		l, r = numlist[len(numlist)//2:], numlist[:len(numlist)//2]
		l = mergesort(l, sorting) # left section 
		r = mergesort(r, sorting) # right section
		i,j,k = 0,0,0 # index for left, right and whole section of the input array
		if sorting == 'x':
			while i < len(l) and j < len(r):
				if l[i][0] <= r[j][0]:
					numlist[k] = l[i]
					i += 1
				else:
					numlist[k] = r[j]
					j += 1
				k += 1
		else:
			while i < len(l) and j < len(r):
				if l[i][1] <= r[j][1]:
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


print('====== X sorted =========')		
x_sorted_list = mergesort(pts)
print(np.asarray(x_sorted_list))
print('====== Y sorted =========')
y_sorted_list = mergesort(pts, 'y')
print(np.asarray(y_sorted_list))