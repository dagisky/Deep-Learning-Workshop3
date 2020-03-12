# strassen's multiplication algorithm
import numpy as np

a = np.random.randint(5, size=(3,3))
b = np.random.randint(5, size=(3,3))
a,b = list(a), list(b)
print('--------product---------')

def mul(x,y):	
	assert len(x) == len(y[0])
	product = list(np.zeros((len(x), len(y[0]))))
	for i in range(len(x)):
		for j in range(len(y[0])):
			for k in range(len(x[0])):
				product[i][j] += x[i][k]*y[k][j]
	return product


m = mul(a,b)
print(np.asarray(m))
