import os
import xmltodict
import dicttoxml
import sys

curpath = os.path.basename(__file__)
sys.path.append(os.path.join(curpath, os.pardir))
from interfaces.IXmlRepository import IXmlRepository

class XmlRepository(IXmlRepository): # Inheriting from the defined interface
    """Module providing a function printing python version."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(XmlRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self, root="root") -> None:
        self.root = root

    def read(self, path_file):
        """
        Read json file.

        Parameters:
        - path_file (string): path of the file xml.

        Returns: TBD.
        """
        try:
            if path_file and os.path.exists(path_file):
                with open(path_file, 'r', encoding="utf-8") as file:
                    content = file.read()
                    xml_data = xmltodict.parse(content)
                    return xml_data[self.root]
        except Exception as ex:
            print("Error: ", ex)
        return None

    def read_all(self, path_folder):
        """
        Read json file.

        Parameters:
        - path_folder (string): path of the folder xml.

        Returns: TBD.
        """
        try:
            objs = []
            if os.path.exists(path_folder) and os.path.isdir(path_folder):
                xml_files = [f for f in os.listdir(
                    path_folder) if f.endswith('.xml')]

                for xmlfile in xml_files:
                    objs.append(self.read(path_folder + "\\" + xmlfile))

                return objs
        except Exception as ex:
            print("Error: ", ex)
        return None

    def create_by_id(self, path_folder, obj):
        """
        Create file with object.

        Parameters:
        - path_folder (string): path of the folder xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)

            pathfile = path_folder + f"\\{obj['_id']}.xml"

            if os.path.exists(pathfile):
                os.remove(pathfile)

            # Convert dictionary to XML string
            xml_string = dicttoxml.dicttoxml(
                obj, custom_root=self.root).decode("utf-8")

            with open(pathfile, 'w', encoding="utf-8") as file:
                file.write(xml_string)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def create_by_name(self, path_file, obj):
        """
        Create by file with object.

        Parameters:
        - path_file (string): path of the file xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if os.path.exists(path_file):
                os.remove(path_file)

            # Convert dictionary to XML string
            xml_string = dicttoxml.dicttoxml(
                obj.__dict__, custom_root=self.root).decode("utf-8")

            with open(path_file, 'w', encoding="utf-8") as file:
                file.write(xml_string)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def create_all(self, path_folder, objs):
        """
        Create all file with object.

        Parameters:
        - path_folder (string): path of the folder xml.
        - objs (list object): list object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)

            if objs:
                for obj in objs:
                    self.create_by_id(path_folder, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def update_by_id(self, path_folder, obj):
        """
        Update file with obj.

        Parameters:
        - path_folder (string): path of the folder xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)

            path_file = path_folder + f"\\{obj['_id']}.xml"
            if os.path.exists(path_file):
                os.remove(path_file)
            self.create_by_name(path_file, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def update_by_name(self, path_file, obj):
        """
        Update json file with specification name in path.

        Parameters:
        - path_file (string): path of the file xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if os.path.exists(path_file):
                os.remove(path_file)
            self.create_by_name(path_file, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def delete(self, path_folder, _id):
        """
        Delete json file with specification name in path.

        Parameters:
        - path_folder (string): path of the file xml.
        - _id (string): id of object.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)

            path_file = path_folder + f"\\{_id}.xml"
            if os.path.exists(path_file):
                os.remove(path_file)

        except Exception as ex:
            print("Error: ", ex)
        return None