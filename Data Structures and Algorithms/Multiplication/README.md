# Matrix Multiplication Algorithms
## Naive Matrix Multiplication 
The normal matrix multiplication runs with O(n^3) time complexity. 
### Defination 
If *A* is an m × n matrix and *B* is an n × p matrix.  
![matrix multiplication](https://wikimedia.org/api/rest_v1/media/math/render/svg/9196c0c24ad20c3b18582bc78785fa405d91c7c3)  
the matrix product C = AB (denoted without multiplication signs or dots) is defined to be the m × p matrix
![matrix mul product](https://wikimedia.org/api/rest_v1/media/math/render/svg/7d3ce5d06e84e1a8575ce6f1d47a90d006baf628)  
Such that  
![eqn](https://wikimedia.org/api/rest_v1/media/math/render/svg/ee372c649dea0a05bf1ace77c9d6faf051d9cc8d)  
### Example
![example](https://www.mathwarehouse.com/algebra/matrix/images/matrix-multiplication/dimensions-of-product-matrix-v2.webp)

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

## Devide and Conquer Mulltiplication
Simple Divide and Conquer method multiplies two square matrices by.
1) Dividing matrices A and B in 4 sub-matrices of size N/2 x N/2 as shown in the below diagram.
2) Calculate following values recursively. ae + bg, af + bh, ce + dg and cf + dh.

![Devide and conquer Matrix Multiplication](https://media.geeksforgeeks.org/wp-content/cdn-uploads/strassen_new.png)

In the above method, we do 8 multiplications for matrices of size N/2 x N/2 and 4 additions. Addition of two matrices takes O(N^2) time. So the time complexity can be written as
```sh
T(N) = 8T(N/2) + O(N^2)  

From Master\'s Theorem, time complexity of above method is O(N3)
which is unfortunately same as the above naive method.
```
## Python Code Sample
```sh
def mul(m1, m2):
	n = len(m1)
	r = np.zeros((n,n))
	a, b, c, d = m1[:n//2,:n//2], m1[:n//2,n//2:], m1[n//2:,:n//2], m1[n//2:,n//2:]
	e, f, g, h = m2[:n//2,:n//2], m2[:n//2,n//2:], m2[n//2:,:n//2], m2[n//2:,n//2:]
	if len(m1) > 2:			
		s11, s12, s21, s22 = mul(a,e)+mul(b,g), mul(a,f)+mul(b,h), mul(c,e)+mul(d,g), mul(c,f)+mul(d,h)
	else:
		s11, s12, s21, s22 = a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h
	r[:n//2,:n//2], r[:n//2,n//2:], r[n//2:,:n//2], r[n//2:,n//2:] = s11, s12, s21, s22
	return r
```

## Strassen's Algorithm (1969)

License
----

None
