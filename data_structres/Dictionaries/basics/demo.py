courses = {"course":"Python",
           "version": 3,
           "Duration": "20 Days"}
print(courses)

print(courses['version'])
print(courses.get('version'))

courses['student'] = 'Wasif'
print(courses)
print()

#Updation
courses['Duration'] = '99 Days'
print(courses)
print()

#Remove or pop operation
print(courses.pop('Duration'))
print(courses)
print()