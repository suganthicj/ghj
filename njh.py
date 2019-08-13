def fact(x1):
	y1=1
	for p in range(1,x1+1):
		y1=y1*p
	return(y1)
x1,z1=map(int,input().split())
print(fact(x1)//fact(x1-z1))
