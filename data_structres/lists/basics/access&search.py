L = [1,2,3,4,5,6,7,8,9]
for item in L:
    print(item, end=' ')

n = len(L)
print()
print("Length of List is: ",n)

for i in range(n):
    print(L[i], end=' ')


#Search
print()
key = int(input("Enter num to be searched: "))

for item in L:
    if item == key:
        print(item, " is found in list")
        break

print(key," is not found in the list")