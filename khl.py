def fact(x1):
	z1=1
	for t in range(1,x1+1):
		z1=z1*t
	return(z1)
x1,y1=map(int,input().split())
print(fact(x1)//(fact(x1-y1)*fact(y1)))
