def reverselist(a):
    print(a[: :-1])

a = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    a.append(ele) # adding the element
      
print(a)
a.sort()
print( "sorted list = ",a)

reverselist(a)
