
ls = [1,2,3,4,5]

ls1 = ls.copy()

# Both lists were at different locations
print(id(ls))
print(id(ls1))

ls1.append(6)
print(ls)
print(ls1)