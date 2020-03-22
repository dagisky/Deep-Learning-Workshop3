import numpy as np
import time

a = np.random.randint(5, size=(8,8))
b = np.random.randint(5, size=(8,8))
print(a)
print(b)
print('--------naive product---------')


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
def strassen(m1, m2):
	n = len(m1)
	r = np.zeros((n,n))
	a, b, c, d = m1[:n//2,:n//2], m1[:n//2,n//2:], m1[n//2:,:n//2], m1[n//2:,n//2:]
	e, f, g, h = m2[:n//2,:n//2], m2[:n//2,n//2:], m2[n//2:,:n//2], m2[n//2:,n//2:]
	if len(m1) > 2:
		p1, p2, p3, p4 = strassen(a,(f-h)), strassen((a+b),h), strassen((c+d),e), strassen(d,(g-e))
		p5, p6, p7 = strassen((a+d),(e+h)), strassen((b-d),(g+h)), strassen((a-c),(e+f))
	else:
		p1, p2, p3, p4 = a*(f-h), (a+b)*h, (c+d)*e, d*(g-e)
		p5, p6, p7 = (a+d)*(e+h), (b-d)*(g+h), (a-c)*(e+f)

	r[:n//2,:n//2], r[:n//2,n//2:], r[n//2:,:n//2], r[n//2:,n//2:] = p5+p4-p2+p5, p1+p2, p3+p4, p1+p5-p3-p7
	return r
start_time = time.time()
m = mul(a,b)
naive_end_time = time.time()
naive_time = naive_end_time - start_time
m2 = mul(a,b)
strassen_time = time.time() - naive_end_time
print(np.asarray(m))
print("---naive method %s seconds ---" % (naive_time))
print('-----------strassen-----------')
print(np.asarray(m2))
print("---strassen method %s seconds ---" % (strassen_time))