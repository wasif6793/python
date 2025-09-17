#The best way to perform modification is to convert tuple into list

country = ("America","India","UAE","Oman","Nepal","Japan")
#conversion to list
temp = list(country)
print(temp)
temp.append("Russia")
print(temp)
print()

temp.sort()
print(temp)
print()


temp.pop()
print(temp)

#convert list to tuple
country = tuple(temp)
print(country)