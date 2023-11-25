import XmlRepository as Xml
import json


class Book(object):
    def __init__(self, author, title, genre, price, description):
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
js = json.loads(_xmlRepository.read(pathFile))

book: list[Book] = js['root']['book']

print(book)
