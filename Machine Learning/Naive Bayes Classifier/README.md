# Naive Bayes classifier
The simplest solutions are usually the most powerful ones, and Naive Bayes is a good example of that. Naive Bayes is a family of probabilistic algorithms that take advantage of probability theory and Bayes’ Theorem (Bayes’ Theorem, which describes the probability of a feature, based on prior knowledge of conditions that might be related to that feature.) to predict the tag of a text (like a piece of news or a customer review). We’re going to be working with an algorithm called Multinomial Naive Bayes.

## Baye’s Theorem
 describes the probability of an event, based on prior knowledge of conditions that might be related to the event.[1] For example, if the probability that someone has cancer is related to their age.
![Baye’s Theorem](https://wikimedia.org/api/rest_v1/media/math/render/svg/87c061fe1c7430a5201eef3fa50f9d00eac78810)
where {\displaystyle A}A and {\displaystyle B}B are events and {\displaystyle P(B)\neq 0}{\displaystyle P(B)\neq 0}.
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

