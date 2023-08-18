from abc import abstractmethod


class EntryDao:
    """
    EntryDao is an abstract class that defines the interface for a single record
    It is used to abstract away the implementation of the data access object from the rest of the application.
    """

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def get_all_rec(self):
        pass

    @abstractmethod
    def insert_new_rec(self, rec: str):
        pass
