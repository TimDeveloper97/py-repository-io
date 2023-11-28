"""abstractmethod lib"""
from abc import abstractmethod


class IXmlRepository:
    """Interface of Xml Repository"""
    
    @abstractmethod
    def read(self, path_file):
        """
        Read json file.

        Parameters:
        - path_file (string): path of the file xml.

        Returns: TBD.
        """

    @abstractmethod
    def read_all(self, path_folder):
        """
        Read json file.

        Parameters:
        - path_folder (string): path of the folder xml.

        Returns: TBD.
        """

    @abstractmethod
    def create_by_id(self, path_folder, obj):
        """
        Create file with object.

        Parameters:
        - path_folder (string): path of the folder xml.
        - obj (object): object to write.

        Returns: TBD.
        """
            
    @abstractmethod
    def create_by_name(self, path_file, obj):
        """
        Create all file with object.

        Parameters:
        - path_file (string): path of the file xml.
        - obj (object): object to write.

        Returns: TBD.
        """
        
    @abstractmethod
    def create_all(self, path_folder, objs):
        """
        Create all file with object.

        Parameters:
        - path_folder (string): path of the folder xml.
        - objs (list object): list object to write.

        Returns: TBD.
        """

    @abstractmethod
    def update_by_id(self, path_folder, obj):
        """
        Create all file with object.

        Parameters:
        - path_folder (string): path of the folder xml.
        - obj (object): object to write.

        Returns: TBD.
        """

    @abstractmethod
    def update_by_name(self, path_file, obj):
        """
        Update json file with specification name in path.

        Parameters:
        - path_file (string): path of the file xml.
        - obj (object): object to write.

        Returns: TBD.
        """

    @abstractmethod
    def delete(self, path_folder, _id):
        """
        Delete json file with specification name in path.

        Parameters:
        - path_folder (string): path of the file xml.
        - _id (string): id of object.

        Returns: TBD.
        """
