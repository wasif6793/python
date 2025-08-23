#create list of squares
#Syntax: [expression for item in iterable if condition]
k = int(input("Enter value of k: "))
sq = [x**2 for x in range(k) if x%2 ==0]
print("List of squares ",sq)
print()


#Normal way example:
pairs = []
for a in [1,2]:
    for b in [3,4]:
        pairs.append((a,b))
print("Normal method: ",pairs)
print()


#List comprehension method
pairs2 = [(c,d) for c in [1,2] for d in [3,4]]
print("Using list comprehension: ",pairs2)
print()
