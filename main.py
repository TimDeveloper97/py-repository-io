import repositories.XmlRepository as xml
import repositories.XmlRepositoryV2 as xml_v2
import json
import repositories.ExcelRepository as excel


class Description:
    def __init__(self, **kwargs):
        # super().__init__(id)
        for key, value in kwargs.items():
            setattr(self, key, value)


class Book(xml.BaseModel):
    def __init__(self, **kwargs):
        super().__init__(id)

        # Check if 'address' key is present in kwargs
        if 'descriptions' in kwargs and kwargs['descriptions'] != None:
            # Create an instance of the Author class using the provided name
            self.descriptions = [Description(**description)
                                 for description in kwargs['descriptions']['description']]
        else:
            self.descriptions = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{0} {1}".format(self.author, self.title)


path_folder = f"O:\\TestData"
path_file = f"O:\\TestData\\book.xml"
path_file_excel = f"O:\\TestData\\example.xlsx"

# excel
# excel.excelRepository().run(pathFolder)
# excel.write_to_excel(path_file_excel)
_xml_repository = xml.XmlRepository()
_xml_repository_v2 = xml_v2.XmlRepositoryV2()
data_object = _xml_repository_v2.read(path_file)
# for obj in data_object:
# for description in obj.descriptions:
# print(description)
# print(description.city, description.zipcode)
for description_group in data_object[0].descriptions:
    for city in description_group.city:
        print(city[0], city[1])
result = _xml_repository.read(path_file)
# print(result)

js = json.loads(result)

print(js['root']['book'])

# books: list[Book](js['root']['book'])
# get object book
# books = [Book(id=b.get('@id'), author=b.get('author'),
#                title=b.get('title'), genre=b.get('genre'), price=b.get('price'),
#                description=b.get('description')) for b in js['root']['book']]
books = [Book(**book_data) for book_data in js['root']['book']]

print(books)
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
