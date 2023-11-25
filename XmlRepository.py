from ast import excepthandler
import os
import xmltodict
import dicttoxml
import json


class BaseModel:
    def __init__(self, id):
        self.id = id


class xmlRepository:
    def __init__(self, root="root") -> None:
        self.root = root

    def read(self, pathFile):
        """
        Read json file.

        Parameters:
        - pathFile (string): path of the file xml.

        Returns: TBD.
        """
        try:
            if pathFile and os.path.exists(pathFile):
                with open(pathFile, 'r') as file:
                    content = file.read()
                    js = json.dumps(xmltodict.parse(content), indent=2)
                    return js
        except Exception as ex:
            print("Error: ", ex)
        return None

    def readAll(self, pathFolder):
        """
        Read json file.

        Parameters:
        - pathFolder (string): path of the folder xml.

        Returns: TBD.
        """
        try:
            files = []
            objs = []
            if os.path.exists(pathFolder) and os.path.isdir(pathFolder):
                xmlfiles = [f for f in os.listdir(
                    pathFolder) if f.endswith('.xml')]

                for xmlfile in xmlfiles:
                    objs.append(self.read(pathFolder + "\\" + xmlfile))

                return objs
        except Exception as ex:
            print("Error: ", ex)
        return None

    def createById(self, pathFolder, obj):
        """
        Create file with object.

        Parameters:
        - pathFolder (string): path of the folder xml.
        - obj (string): object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(pathFolder):
                os.makedirs(pathFolder)

            pathfile = pathFolder + f"\\{obj.id}.xml"

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

    def createByName(self, pathFile, obj):
        """
        Ccreate all file with object.

        Parameters:
        - pathFile (string): path of the file xml.
        - obj (string): object to write.

        Returns: TBD.
        """
        try:
            if os.path.exists(pathFile):
                os.remove(pathFile)

            # Convert JSON string to Python dictionary
            json_data = json.dumps(obj.__dict__)

            # Convert dictionary to XML string
            xml_string = dicttoxml.dicttoxml(
                json_data, custom_root=self.root).decode("utf-8")

            with open(pathFile, 'w') as file:
                file.write(xml_string)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def createAll(self, pathFolder, objs):
        """
        Ccreate all file with object.

        Parameters:
        - pathFolder (string): path of the folder xml.
        - objs (string): list object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(pathFolder):
                os.makedirs(pathFolder)

            if objs:
                for obj in objs:
                    self.createById(pathFolder, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def updateById(self, pathFolder, obj):
        """
        Ccreate all file with object.

        Parameters:
        - pathFolder (string): path of the folder xml.
        - obj (string): object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(pathFolder):
                os.makedirs(pathFolder)

            pathFile = pathFolder + f"\\{obj.id}.xml"
            if os.path.exists(pathFile):
                os.remove(pathFile)
            self.createByName(pathFile, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def updateByName(self, pathFile, obj):
        """
        Create json file with specification name in path.

        Parameters:
        - pathFile (string): path of the file xml.
        - obj (string): object to write.

        Returns: TBD.
        """
        try:
            if os.path.exists(pathFile):
                os.remove(pathFile)
            self.createByName(pathFile, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def delete(self, pathFolder, id):
        """
        Create json file with specification name in path.

        Parameters:
        - pathFile (string): path of the file xml.
        - obj (string): object to write.

        Returns: TBD.
        """
        try:
            if not os.path.exists(pathFolder):
                os.makedirs(pathFolder)

            pathFile = pathFolder + f"\\{id}.xml"
            if os.path.exists(pathFile):
                os.remove(pathFile)

        except Exception as ex:
            print("Error: ", ex)
        return None
