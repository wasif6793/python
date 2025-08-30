#Loop through a list

fruits  = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

#Loop with range

for i in range(5): #[0,1,2,3,4]
    print(i)

#syntax while

#while True:
    #code block

count = 5
while count > 0:
    print(count)
    count-=1

#Break statement

for i in range(10):
    if i == 7:
        break
    print(i)

#Continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)

