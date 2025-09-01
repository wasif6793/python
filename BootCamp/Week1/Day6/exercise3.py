#Write a program to copy the contents of one file to another
def copy_files(filename1,filename2):
    try:
        with open(filename1,'r') as file1, open(filename2,"w") as file2:
                for line in file1:
                    file2.write(line)
    except FileNotFoundError:
        print("File not found")

def printfile2(filename):
    try:
        with open(filename,'r') as file:
            items = file.readlines()
            for item in items:
                print(item)
    except FileNotFoundError:
        print("File ni mila")

fl2 = "Sample1.txt"
fl1 = "Sample.txt"
copy_files(fl1,fl2)
printfile2(fl2)

