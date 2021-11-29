
#let's do a Fibonacci series...
#start with 0 and 1 
fibb=[0,1]
fibb[0] = 0
fibb[1] = 1
maxvar=20 #num of slots from 0 to end
##TO DO: ADD INPUT of maxvar!!###########
#def fibin(maxvar)
for countval in range(2,maxvar):
	#must use insert to add values to the list
	fibb.insert((countval),fibb[countval-1]+fibb[countval-2])
	print(fibb)
		

	
