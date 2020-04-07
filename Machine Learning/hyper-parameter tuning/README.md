# Machine Learning
## Doing XGBoost hyper-parameter tuning the smart way 
Here we introduce three general purpose discrete optimization algorithms aimed at search for the optimal hyper-param combination: grid-search, coordinate descent and genetic algorithms. we will focus on optimizing XGBoost hyper-parameters in our experiment However, pretty much all of what is discussed here applies to any other advanced ML algorithms.

Usually, the more flexible and powerful an algorithm is, the more design decisions and adjustable hyper-parameters it will have. These are parameters specified by “hand” to the algo and fixed throughout a training pass.

 In tree-based models, hyper-parameters include things like the maximum depth of the tree, the number of trees to grow, the number of variables to consider when building each tree, the minimum number of samples on a leaf, the fraction of observations used to build a tree, and a few others. For neural networks, the list includes the number of hidden layers, the size (and shape) of each layer, the choice of activation function, the drop-out rate and the L1/L2 regularization constants.

 ![hyper param eq](https://miro.medium.com/max/1084/1*WjmgwZBjiWfbUmgCAwPvMg.png)


#### Introducing the Hyper-Parameter Grid

One important thing to note about hyper-parameters is that, often, they take on discrete values, with notable exceptions being things like drop-out rates or regularization constants. Thus, for practical reasons and to avoid the complexities involved in doing hybrid continuous-discrete optimization, most approaches to hyper-parameter tuning start off by discretizing the ranges of all hyper-parameters in question. For example, for our XGBoost experiments below we will fine-tune five hyperparameters. The ranges of possible values that we will consider for each are as follows:

```sh
{"learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
 "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
 "min_child_weight" : [ 1, 3, 5, 7 ],
 "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
 "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ] }
```


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
