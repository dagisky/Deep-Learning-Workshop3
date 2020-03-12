# Algorithms
## Matrix Multiplication 
The normal matrix multiplication runs with O(n^3) time complexity. 
### Defination 
If *A* is an m × n matrix and *B* is an n × p matrix.  
[![matrix multiplication](https://wikimedia.org/api/rest_v1/media/math/render/svg/9196c0c24ad20c3b18582bc78785fa405d91c7c3)]  
the matrix product C = AB (denoted without multiplication signs or dots) is defined to be the m × p matrix
[![matrix mul product](https://wikimedia.org/api/rest_v1/media/math/render/svg/7d3ce5d06e84e1a8575ce6f1d47a90d006baf628)]  
Such that  
![eqn](https://wikimedia.org/api/rest_v1/media/math/render/svg/ee372c649dea0a05bf1ace77c9d6faf051d9cc8d)  
### Example
[![example](https://www.mathwarehouse.com/algebra/matrix/images/matrix-multiplication/dimensions-of-product-matrix-v2.webp)]

## Python Code Sample

```sh
def mul(x,y):	
	assert len(x) == len(y[0])
	product = list(np.zeros((len(x), len(y[0]))))
	for i in range(len(x)):
		for j in range(len(y[0])):
			for k in range(len(x[0])):
				product[i][j] += x[i][k]*y[k][j]
	return product
```

Java Code is also provided.

License
----

None
