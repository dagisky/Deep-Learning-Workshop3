import numpy as np

a = np.random.randint(5, size=(4,4))
b = np.random.randint(5, size=(4,4))
print(a)
print(b)
print('--------dot product---------')


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

m = mul(a,b)
print(np.asarray(m))
