class Book(object):
    def __init__(self,title,author):
        self._title=title
        self._author=author

    def gettitle(self):
        return self._title
    
    def settitle(self,newtitle):
        self._title=newtitle

    title= property(gettitle,settitle)

    def getauthor(self):
        return self._
    
    def setauthor(self,newauthor):
        self._author=newauthor

    title= property(getauthor,setauthor)

    def __str__(self):
        return ("The Title of the book is %s and the Author is %s"%(self._title,self._author))
    

    