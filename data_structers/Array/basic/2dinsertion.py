from array import *
ar2 = [[1,2,3],[4,5,6],[7,8,9]]
ar2.insert(1,[10,11,12])
print(ar2)
for r in ar2:
    for c in r:
        print(c,end=" ")
    print()
