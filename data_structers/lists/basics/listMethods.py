#append() - appends element to list
l1 = []
l1.append(1)
l1.append(2)
l1.append(3)

print(l1)

#clear() -makes list empty
l1.clear()
print(l1)
print()

#copy()
l1 = [1,2,3,4,5,7,7,6,7,8,9]
l2 = l1.copy()
print(id(l1))
print(id(l2))
print(l1)
print(l2)
print()

#count()
x = 7
print("count method ",l1.count(x))
print()

#extend()
l2 = [7,6,5,4,3,2,1]
l1.extend(l2)
print(l1)
print()

#list1.index(x)
list1 = ["A","B","C","D"]
ind = list1.index("C")
print("Index: ",ind)
print()

#list1.insert(i,x)
x = 55
index = 2
list1.insert(index, x)
print("Insert operation: ",list1)
print()

#list1.pop() - Remove & returns the last element
print("Original List:", list1)
list1.pop()
print("List after pop operation: ",list1)
print()

#list1.remove(x)
print("List before remove operation :",list1)
list1.remove("B")
print("After remove operation: ",list1)
print()

#reverse()

print("List without reverse: ",list1)
list2 = list1.reverse()
print("Nothing happens",list2)
print("Nothing happens ",list1.reverse())
list1.reverse()
print("Reversed ",list1)
print()

#list.sort()
list1 = [1,2,54,3,6,4,9]
list1.sort()
print("Ascending sorting ",list1)
#reverse sorting
list1.sort(reverse=True)
print("Descending sorting ",list1)