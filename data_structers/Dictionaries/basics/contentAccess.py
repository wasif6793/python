from traceback import print_tb

courses =dict( {"course":"Python",
           "version": 3,
                'fee': 5000,
           "Duration": "20 Days"})

for key,value in courses.items():
    print(key,value)
print()

# Or we can access like that
for key in courses:
    print(key,courses[key])
print()

#To access keys
for key in courses.keys():
    print('key:',key)

print()

#To access the values
for value in courses.values():
    print('Value:',value)
