import xml.etree.ElementTree as ET


class DynamicObject:
    def __init__(self, element):
        self._parse_element(element)

    def _parse_element(self, element):
        for child in element:
            # If the child has no sub-elements, set its text as an attribute
            if not list(child):
                setattr(self, child.tag, child.text.strip())
            else:
                # If the attribute doesn't exist, create a list attribute
                if not hasattr(self, child.tag):
                    setattr(self, child.tag, [])

                # Append a new DynamicObject or a value to the list
                getattr(self, child.tag).append(DynamicObject(
                    child) if list(child) else child.text.strip())


def xml_to_object(xml_data):
    root = ET.fromstring(xml_data)
    return [DynamicObject(book) for book in root.findall('book')]


xml_data = """<root>
   <book>
      <id>bk111</id>
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <descriptions>
         <description>
            <city>New York</city>
            <zipcode>10001</zipcode>
         </description>
         <description>
            <city>Los Angeles</city>
            <zipcode>90001</zipcode>
         </description>
      </descriptions>
   </book>
   <book>
      <id>bk112</id>
      <author>Another Author</author>
      <title>Another Book</title>
      <genre>Fiction</genre>
      <price>29.99</price>
      <publish_date>2022-01-01</publish_date>
      <descriptions>
         <description>
            <city>Chicago</city>
            <zipcode>60601</zipcode>
         </description>
         <description>
            <city>Boston</city>
            <zipcode>02101</zipcode>
         </description>
      </descriptions>
   </book>
</root>"""

books = xml_to_object(xml_data)

# Accessing attributes for the first book
first_book = books[0]
print(first_book.id)
print(first_book.author)
print(first_book.title)
print(first_book.genre)
print(first_book.price)
print(first_book.publish_date)

# Accessing nested elements for the first book
for description in first_book.descriptions:
    print(description.city, description.zipcode)
