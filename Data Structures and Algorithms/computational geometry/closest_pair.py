import numpy as np 
import math
pts = np.random.randint(20, size=(10,2))
print(pts)

def Euclidean_Distance(a, b):
	return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


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
    return minimum_distance, Target_Pair


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

def Closest_Pair(Px, Py):
	if len(Px) <= 3:
		return BruteForceClosestPair(Px)

	midpoint_x = len(Px) // 2 # int division of lenght of the x sorted array
	Qx = Px[:midpoint_x]
	Rx = Px[midpoint_x:]
	median_x = Px[midpoint_x]
	Qy,Ry = [], []

	for point in Py:
		if point[0] < int(median_x[0]):
			Qy.append(point)
		else:
			Ry.append(point)

	min_distance_Left = Closest_Pair(Qx,Qy)
	min_distance_Right = Closest_Pair(Rx,Ry) 
	
	if min_distance_Left[0] <= min_distance_Right[0]:
		min_distance = min_distance_Left
	else:
		min_distance = min_distance_Right   
	# min_distance = min(min_distance_Left, min_distance_Right)

	x_bar = Qx[-1][0]
	Sy = []
	for y in Py:
		if x_bar - min_distance[0] < y[0] < x_bar + min_distance[0]:
			Sy.append(y)
	best_pair = (0, 0)
	for i in range(len(Sy)-1):
		for j in range(i+1, min(i+7, len(Sy))):
			dist = Euclidean_Distance(Sy[i], Sy[j])
			if dist < min_distance[0]:
				min_distance = (dist, Sy[i], Sy[j])
	return min_distance

def Initial_Sort(P):
    Px = mergesort(P,'x')
    Py = mergesort(P,'y')
    return Px,Py



print('====== Brute Force Shortest path =========')
dist, xy = BruteForceClosestPair(pts)
print((dist, xy))
print('====== Divide and Conquer =========')
Px, Py = Initial_Sort(pts)
dist, x, y = Closest_Pair(Px, Py)
print((dist, x, y))