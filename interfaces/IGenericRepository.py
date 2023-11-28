"""abstractmethod lib"""
from abc import abstractmethod


class IGenericRepository:
    """Interface of Xml GenericRepository"""

    @abstractmethod
    def add(self, obj):
        """
        Create file with content obj in folderId.

        Parameters:
        - obj (string): object to write.

        Returns: TBD.
        """

    @abstractmethod
    def get(self, _id):
        """
        Get file with _id in folderId.

        Parameters:
        - _id (string): _id of file xml.

        Returns: TBD.
        """

    @abstractmethod
    def get_all(self):
        """
        Get all file in folderId.

        Returns: TBD.
        """

    @abstractmethod
    def exist(self, path_folder, _id = None):
        """
        Checked exist file with id in folderId.

        Parameters:
        - path_folder (string): pathFolder.
        - _id (string): id of file xml.

        Returns: TBD.
        """

    @abstractmethod
    def update(self, obj):
        """
        Update exist file with obj.id in folderId.

        Parameters:
        - obj (object): object to write.

        Returns: TBD.
        """

    @abstractmethod
    def delete(self, _id):
        """
        Delete exist file with id in folderId.

        Parameters:
        - _id (string): _id of file xml.

        Returns: TBD.
        """

    @abstractmethod
    def delete_all(self):
        """
        Delete all in path.

        Returns: TBD.
        """
