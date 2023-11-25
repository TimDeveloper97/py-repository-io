import XmlRepository as Xml
import json


class Book:
    def __init__(self, id, author, title, genre, price, description):
        self.id = id
        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
        self.description = description

    def __str__(self):
        return "{0} {1}".format(self.author, self.title)


pathFolder = f"O:\\TestData"
pathFile = f"O:\\TestData\\book.xml"

_xmlRepository = Xml.XmlRepository()
result = _xmlRepository.read(pathFile)
print(result)
js = json.loads(result)

print(js)

# books: list[Book](js['root']['book'])

book1s = [Book(id=b.get('@id'), author=b.get('author'),
               title=b.get('title'), genre=b.get('genre'), price=b.get('price'),
               description=b.get('description')) for b in js['root']['book']]
# books = [Book(**book_data) for book_data in data_list]

for book in book1s:
    print(f"Title: {book.title}, Author: {book.author}")
print("hello world")
