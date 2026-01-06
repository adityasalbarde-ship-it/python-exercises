class library:
    def __init__(self):
        self.books = []
        self.nobooks = 0

    def addbook(self, book):
            self.books.append(book)
            self.nobooks = len(self.books)

    def showinfo(self):
      print(f"the library has {self.nobooks} books. the books are")
      for book in self.books:
        print(book)

l1 = library()
l1.addbook("harry potter1")
l1.addbook("harry potter2")
l1.addbook("harry potter3")
l1.addbook("harry potter4")
l1.showinfo()
               
        
