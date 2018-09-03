class Book:
    def __init__(self,title,author,path):
        self.title=title
        self.author=author
        self.path=path
    def __repr__(self):
        return '<title={} author={} path={}>'.format(self.title,self.author,self.path)


def get_all_books():
    books = []
    for i in range(10):
        book = Book('item{}'.format(i),'author{}'.format(i),'path{}'.format(i))
        books.append(book)
    return books

books=get_all_books()

s=1


