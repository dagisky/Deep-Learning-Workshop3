# Algorithms
## Closest Pair
The distance between two points in 2D space can be calculated by Euclidean Distance.
![Euclidean Distance](https://miro.medium.com/max/332/1*jLnjJB8aAs4JPCgZAx8-Yw.jpeg)
First of all, We need to think about the Brute Force solution which is just iterate in a double For Loop and check all points. But can we do better? The answer is yes. Using the Magic of divide and conquer technique we can achieve better.
### Example
Given an array of  x = ( 5, 1, 4, 2, 8 )
#### First Pass
- ( **5**, **1**, 4, 2, 8, ) –> ( **1**, **5**, 4, 2, 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
- ( 1, **5**, **4**, 2, 8 ) –>  ( 1, **4**, **5**, 2, 8 ), Swap since 5 > 4
- ( 1, 4, **5**, **2**, 8 ) –>  ( 1, 4, **2**, **5**, 8 ), Swap since 5 > 2
- ( 1, 4, 2, **5**, **8** ) –> ( 1, 4, 2, **5**, **8** ), Now, since these elements are already in order (8 > 5), algorithm does not swap them

#### Second Pass:
- ( **1**, **4**, 2, 5, 8 ) –> ( **1**, **4**, 2, 5, 8 )
- ( 1, **4**, **2**, 5, 8 ) –> ( 1, **2**, **4**, 5, 8 ), Swap since 4 > 2
- ( 1, 2, **4**, **5**, 8 ) –> ( 1, 2, **4**, **5**, 8 )
- ( 1, 2, 4, **5**, **8** ) –>  ( 1, 2, 4, **5**, **8** )

Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted. Thus the algorithm will go on to the third pass

## Python Code Sample

```sh
def bubble_sort(num_list):
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

Java Code is also provided.

License
----

None
