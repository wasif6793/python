#Word frequency counter

sentence = input("Enter a sentence: ")

#split sentence into words
words = sentence.split()

#inititalize an empty dictionary
word_count ={}

#count word frequency
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)