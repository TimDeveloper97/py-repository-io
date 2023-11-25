import os
import json
import xmlRepository as xml


class genericRepository:

    def __init__(self, root="root") -> None:
        self.root = root

    def add(folderId, obj):
        """
        Create file with content obj in folderId.

        Parameters:
        - folderId (string): id of folder to write file.
        - obj (string): object to write.

        Returns: TBD.
        """
        try:
            print("")
        except Exception as ex:
            print("Error: ", ex)
        return None

    def get(folderId, id):
        """
        Get file with id in folderId.

        Parameters:
        - folderId (string): id of folder to write file.
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            print("")
        except Exception as ex:
            print("Error: ", ex)
        return None

    def getAll(folderId):
        """
        Get all file in folderId.

        Parameters:
        - folderId (string): id of folder to write file.

        Returns: TBD.
        """
        try:
            print("")
        except Exception as ex:
            print("Error: ", ex)
        return None

    def exist(folderId, id):
        """
        Checked exist file with id in folderId.

        Parameters:
        - folderId (string): id of folder to write file.
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            print("")
        except Exception as ex:
            print("Error: ", ex)
        return None

    def update(folderId, obj):
        """
        Update exist file with obj.id in folderId.

        Parameters:
        - folderId (string): id of folder to write file.
        - obj (object): object to write.

        Returns: TBD.
        """
        try:
            print("")
        except Exception as ex:
            print("Error: ", ex)
        return None

    def delete(folderId, id):
        """
        Delete exist file with id in folderId.

        Parameters:
        - folderId (string): id of folder to write file.
        - id (string): id of file xml.

        Returns: TBD.
        """
        try:
            print("")
        except Exception as ex:
            print("Error: ", ex)
        return None

    def deleteAll(folderId):
        """
        Delete folderId.

        Parameters:
        - folderId (string): id of folder to write file.

        Returns: TBD.
        """
        try:
            print("")
        except Exception as ex:
            print("Error: ", ex)
        return None
