<<<<<<< HEAD
#let's do a Fibonacci series...
=======
#hello, let's do a Fibonacci series...
>>>>>>> 52af6d368f51bd4c7bbeb2febf060cf828c02bbf
#start with 0 and 1 
fibb=[0,1]
fibb[0] = 0
fibb[1] = 1
maxvar=20 #num of slots from 0 to end
#def fibin(maxvar)
for countval in range(2,maxvar):
	#must use insert to add values to the list
	fibb.insert((countval),fibb[countval-1]+fibb[countval-2])
	print(fibb)
		

	