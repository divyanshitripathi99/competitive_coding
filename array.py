def rotate(L,d,n):
	k=L.index(d)
	new_lis=[]
	new_lis=L[k+1:]+L[0:k+1]
	return new_lis

d = 2
n = 7
print(rotate([1,2,3,4,5,6,7],d,n))
