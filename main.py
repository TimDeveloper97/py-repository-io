import repositories.xmlRepository as xml
import json
import time
import repositories.excelRepository as excel
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Book(xml.BaseModel):
    def __init__(self, id, author, title, genre, price, description):
        super().__init__(id)

        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
        self.description = description

    def __str__(self):
        return "{0} {1}".format(self.author, self.title)


pathFolder = f"O:\\TestData"
pathFile = f"O:\\TestData\\book.xml"
pathFileExcel = f"O:\\TestData\\example.xlsx"

# excel
# excel.excelRepository().run(pathFolder)
excel.write_to_excel(pathFileExcel)

_xmlRepository = xml.xmlRepository()
# result = _xmlRepository.read(pathFile)
# print(result)

# js = json.loads(result)

# print(js)

# books: list[Book](js['root']['book'])
# get object book
# books = [Book(id=b.get('@id'), author=b.get('author'),
#                title=b.get('title'), genre=b.get('genre'), price=b.get('price'),
#                description=b.get('description')) for b in js['root']['book']]
# books = [Book(**book_data) for book_data in data_list]

# get list object books
# books = [Book(id=b.get('@id'), author=b.get('author'),
#               title=b.get('title'), genre=b.get('genre'), price=b.get('price'),
#               description=b.get('description')) for b in js['root']['book']]
# book = books[0]
# x = _xmlRepository.createById(
#     pathFolder=pathFolder, obj=book)

# _xmlRepository.delete(pathFolder, books[0].id)
# for book in books:
# print(f"Title: {book.title}, Author: {book.author}")
