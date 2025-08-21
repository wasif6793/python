str =input("Write your name: ")
print("Hello",str)


# Looping

ind  = 0
while(ind < len(str)):
    ch = str[ind]
    print(ch, end=' ')
    ind += 1

# using for loop
print()
for chr in str:
    print(chr, end=' ')

# looping and counting
count = 0
for chr in str:
    if chr == 'a':
        count += 1
print()
print(count)