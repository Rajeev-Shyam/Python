from book import Book

class Ebook(Book):
    def __init__(self, title, author,format):
        super().__init__(title, author)
        self._format=format 

    def getformat(self):
        return self._format
    
    def setformat(self,newformat):
        self._format=newformat
    
    format= property(getformat,setformat)

    def __str__(self):
        return ("The format of the Ebook is %s"%(self._format))