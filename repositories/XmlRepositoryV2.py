import os
import xmltodict
import dicttoxml
import json
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
                child_objects = [DynamicObject(sub_child) for sub_child in child] if list(
                    child) else child.text.strip()
                getattr(self, child.tag).extend(child_objects)


class XmlRepositoryV2:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(XmlRepositoryV2, cls).__new__(cls)
        return cls._instance

    def __init__(self, root="root") -> None:
        self.root = root

    def read(self, path_file):
        """
        Read json file.

        Parameters:
        - pathFile (string): path of the file xml.

        Returns: TBD.
        """
        try:
            if path_file and os.path.exists(path_file):
                with open(path_file, 'r') as file:
                    xml_data = file.read()
                    root = ET.fromstring(xml_data)
                    return [DynamicObject(element) for element in root]
        except Exception as ex:
            print("Error: ", ex)
        return None

    def readAll(self, path_folder):
        """
        Read json file.

        Parameters:
        - pathFolder (string): path of the folder xml.

        Returns: TBD.
        """
        try:
            files = []
            objs = []
            if os.path.exists(path_folder) and os.path.isdir(path_folder):
                xmlfiles = [f for f in os.listdir(
                    path_folder) if f.endswith('.xml')]

                for xmlfile in xmlfiles:
                    objs.append(self.read(path_folder + "\\" + xmlfile))

                return objs
        except Exception as ex:
            print("Error: ", ex)
        return None

    def createById(self, path_folder, obj):
        """
        Create file with object.

        Parameters:
        - pathFolder (string): path of the folder xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)

            pathfile = path_folder + f"\\{obj.id}.xml"

            if os.path.exists(pathfile):
                os.remove(pathfile)

            # Convert JSON string to Python dictionary
            json_data = json.dumps(obj.__dict__)

            # Convert dictionary to XML string
            xml_string = dicttoxml.dicttoxml(
                json_data, custom_root=self.root).decode("utf-8")

            with open(pathfile, 'w') as file:
                file.write(xml_string)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def createByName(self, path_file, obj):
        """
        Ccreate all file with object.

        Parameters:
        - pathFile (string): path of the file xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if os.path.exists(path_file):
                os.remove(path_file)

            # Convert JSON string to Python dictionary
            json_data = json.dumps(obj.__dict__)

            # Convert dictionary to XML string
            xml_string = dicttoxml.dicttoxml(
                json_data, custom_root=self.root).decode("utf-8")

            with open(path_file, 'w') as file:
                file.write(xml_string)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def createAll(self, path_folder, objs):
        """
        Ccreate all file with object.

        Parameters:
        - pathFolder (string): path of the folder xml.
        - objs (list object): list object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)

            if objs:
                for obj in objs:
                    self.createById(path_folder, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def updateById(self, path_folder, obj):
        """
        Ccreate all file with object.

        Parameters:
        - pathFolder (string): path of the folder xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)

            pathFile = path_folder + f"\\{obj.id}.xml"
            if os.path.exists(pathFile):
                os.remove(pathFile)
            self.createByName(pathFile, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def updateByName(self, path_file, obj):
        """
        Create json file with specification name in path.

        Parameters:
        - pathFile (string): path of the file xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if os.path.exists(path_file):
                os.remove(path_file)
            self.createByName(path_file, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def delete(self, path_folder, id):
        """
        Create json file with specification name in path.

        Parameters:
        - pathFile (string): path of the file xml.
        - obj (string): object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)

            pathFile = path_folder + f"\\{id}.xml"
            if os.path.exists(pathFile):
                os.remove(pathFile)

        except Exception as ex:
            print("Error: ", ex)
        return None


# Example usage:
xml_data = """<root>
   <book>
      <id>bk111</id>
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <descriptions>
            <citys>
               <city>asdasdasd</city>
               <city>asdqweqwe</city>
            </citys>
            <zipcode>10001</zipcode>
         </descriptions>
         <descriptions>
            <citys>
               <city>123123152asdasd</city>
               <city>2qrqwrajkhf</city>
            </citys>
            <zipcode>90001</zipcode>
         </descriptions>
   </book>
</root>"""
x = xmltodict.parse(xml_data)['root']
data_object = [DynamicObject(element) for element in (ET.fromstring(xml_data))]

# Accessing attributes
print(data_object)
