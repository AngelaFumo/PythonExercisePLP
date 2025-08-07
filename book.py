class Book:
    title="Antes do mundo nascer"
    typeB="rommance"

    def __init__(self, title, typeB):
        self.title=title
        self.typeB=typeB

    def description(self):
            return "this book is digital"
    

class Romance (Book):
        pass

        def description(self):
            return "this book is pysical"
        

book= Book ("Antes do mundo nascer", "Romance")
print(book.description())
