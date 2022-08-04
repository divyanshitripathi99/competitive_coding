def smalls(lst , d ):
    lst.sort()
    print(lst)
    smalld = lst[d-1]
    print( "THE SMALLEST NO IS =", smalld)

smalls([56, 67,4,6,89],3)