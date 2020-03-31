# Algorithms
## Closest Pair
The distance between two points in 2D space can be calculated by Euclidean Distance.
![Euclidean Distance](https://miro.medium.com/max/332/1*jLnjJB8aAs4JPCgZAx8-Yw.jpeg)
First of all, We need to think about the Brute Force solution which is just iterate in a double For Loop and check all points. But can we do better? The answer is yes. Using the Magic of divide and conquer technique we can achieve better.

In the beginning, We are going to use merge sort. We will sort the points Two Times into two separate array , one sorted according to X-coordinates ascendingly into Px and the other according to Y-coordinates ascendingly into Py.

The next step is to split Px into two parts , Q and R. So now we want to again create Qx,Qy and Rx,Ry each ordered by x,y coordinates respectively.

![Devide in to Q and R](https://miro.medium.com/max/1400/1*7EZNy1w4YDuU4BtJSXJL3Q.png)

## Python Code Sample

```sh
def bubble_sort(num_list):def Euclidean_Distance(a, b):
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
    return minimum_distance,Target_Pair
	n = len(num_list)
	# Traverse through all array elements
	for i in range(n):
		# The last elements are already in place
		for j in range(0, n-i-1):
			# Traverse the array from 0 to n-i-1
			# Swap if the element is found greater than the 
			# next element
			if num_list[j] > num_list[j+1]:
				num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
	return num_list
```

Java Code will also be provided.

License
----

None
