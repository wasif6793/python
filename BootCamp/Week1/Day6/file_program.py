# r | w | a | r+
with open("Sample.txt","w") as file:
    file.write("Hello Worldwa")
    file.writelines(["Wasif", "Sheikh", "MTech"])

with open("Sample.txt","r") as file:
    content1 =file.readline()
    content = file.read()
    print(content)

#Exception handling

try:
    with open("Sample.txt","r") as file:
        content2 = file.read()
except FileNotFoundError:
    print("File not found")


