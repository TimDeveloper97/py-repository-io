import os
import uuid
import shutil
from XmlRepository import XmlRepository

class GenericRepository:
    """Interface of Xml Repository"""
    def __init__(self, root, commany, table=None) -> None:
        self.root = root
        self.commany = commany
        self.table = table
        self._xml = XmlRepository()

    @property
    def path_folder(self):
        """Interface of Xml Repository"""
        if self.table is not None:
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
            if self.path_folder and os.path.exists(self.path_folder):
                if not obj.id:
                    obj.id = str(uuid.uuid4())

                self._xml.create_by_id(self.path_folder, obj)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def get(self, _id):
        """
        Get file with id in folderId.

        Parameters:
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            if self.exist(self.path_folder, _id):
                path_file = self.path_folder + f"{_id}.xml"

                xml_file = self._xml.read(path_file)
                return xml_file
        except Exception as ex:
            print("Error: ", ex)
        return None

    def get_all(self):
        """
        Get all file in folderId.

        Returns: TBD.
        """
        try:
            if self.exist(self.path_folder):
                xml_files = self._xml.readAll(self.path_folder)
                return xml_files
        except Exception as ex:
            print("Error: ", ex)
        return None

    def exist(self, path_folder, _id = None):
        """
        Checked exist file with id in folderId.

        Parameters:
        - pathFolder (string): pathFolder.
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            if not os.path.exists(path_folder):
                return False

            if not _id:
                path_file = path_folder + f"{_id}.xml"
                return os.path.exists(path_file)
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
            if self.exist(self.path_folder):
                path_file = self.path_folder + f"{obj['_id']}.xml"
                self._xml.updateById(path_file)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def delete(self, _id):
        """
        Delete exist file with id in folderId.

        Parameters:
        - folderId (string): id of folder to write file.
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            if self.exist(self.path_folder):
                path_file = self.path_folder + f"{_id}.xml"
                self._xml.delete(path_file, _id)
        except Exception as ex:
            print("Error: ", ex)
        return None

    def delete_all(self):
        """
        Delete folderId.

        Parameters:
        - folderId (string): id of folder to write file.

        Returns: TBD.
        """
        try:
            if self.exist(self.path_folder):
                shutil.rmtree(self.path_folder)
        except Exception as ex:
            print("Error: ", ex)
        return None
