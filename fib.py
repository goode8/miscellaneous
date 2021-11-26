#hello, let's do a Fibonacci series...
fibb=[0,1]
fibb[0] = 0
fibb[1] = 1
maxvar=20 #num of slots from 0..
#def fibin(maxvar)
for countval in range(2,maxvar):
	fibb.insert((countval),fibb[countval-1]+fibb[countval-2])
	print(fibb)
		

	