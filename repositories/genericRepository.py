import os
import json
import xmlRepository as xml
import uuid
import shutil


class genericRepository:

    def __init__(self, root, commany, table=None) -> None:
        self.root = root
        self.commany = commany
        self.table = table
        self._xml = xml.xmlRepository()

    @property
    def pathFolder(self):
        if self.table != None:
            return self.root + f"\\{self.commany}\\{self.table}\\"
        else:
            return self.root + f"\\{self.commany}\\"

    def add(self, obj):
        """
        Create file with content obj in folderId.

        Parameters:
        - obj (string): object to write.

        Returns: TBD.
        """
        try:
            if self.pathFolder and os.path.exists(self.pathFolder):
                if not obj.id:
                    obj.id = str(uuid.uuid4())

                self._xml.createById(self.pathFolder, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def get(self, id):
        """
        Get file with id in folderId.

        Parameters:
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            if self.exist(self.pathFolder, id):
                pathFile = self.pathFolder + f"{id}.xml"

                xmlFile = self._xml.read(pathFile)
                return xmlFile
        except Exception as ex:
            print("Error: ", ex)
        return None

    def getAll(self):
        """
        Get all file in folderId.

        Returns: TBD.
        """
        try:
            if self.exist(self.pathFolder):
                xmlFiles = self._xml.readAll(self.pathFolder)
                return xmlFiles
        except Exception as ex:
            print("Error: ", ex)
        return None

    def exist(self, pathFolder, id=None):
        """
        Checked exist file with id in folderId.

        Parameters:
        - pathFolder (string): pathFolder.
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            if not os.path.exists(pathFolder):
                return False

            if id != None:
                pathFile = pathFolder + f"{id}.xml"
                return os.path.exists(pathFile)
        except Exception as ex:
            print("Error: ", ex)
        return True

    def update(self, obj):
        """
        Update exist file with obj.id in folderId.

        Parameters:
        - folderId (string): id of folder to write file.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            if self.exist(self.pathFolder):
                pathFile = self.pathFolder + f"{id}.xml"
                self._xml.updateById(pathFile)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def delete(self, id):
        """
        Delete exist file with id in folderId.

        Parameters:
        - folderId (string): id of folder to write file.
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            if self.exist(self.pathFolder):
                pathFile = self.pathFolder + f"{id}.xml"
                self._xml.delete(pathFile)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def deleteAll(self, folderId):
        """
        Delete folderId.

        Parameters:
        - folderId (string): id of folder to write file.

        Returns: TBD.
        """
        try:
            if self.exist(self.pathFolder):
                shutil.rmtree(self.pathFolder)
        except Exception as ex:
            print("Error: ", ex)
        return None
