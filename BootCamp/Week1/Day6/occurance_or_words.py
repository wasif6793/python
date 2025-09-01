#Program that counts the number of occurances of a specific word in a text file

def occurance(filename,word):
    count = 0
    try:
        with open(filename,'r') as file:
            for line in file:
                words = line.lower().split()
                count += words.count(word.lower())
        print(count)
    except FileNotFoundError:
        print('File ni mila')

fl = "Sample.txt"
occurance(fl,"Apple")

