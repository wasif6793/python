class Book:
    def __init__(self,title,author="Unknown"):
        self.title = title
        self.author = author

    def details(self):
        return f"{self.title} written by {self.author}"

myBook = Book("Wings of Fire","APJ Abdul Kalam")
authorBook = Book("Lallu Das")

print(myBook.details())
print(authorBook.details())
