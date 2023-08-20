"""
MysqlDao

This module provides an implementation of EntryDao using MySQL as the underlying database.

Classes:
- MysqlDao: Implements EntryDao and interacts with MySQL to perform CRUD operations on the 'tower' table.

"""

from dao.EntryDao import EntryDao
from models.TwEntry import TWEntryRecord
import traceback
import mysql.connector


class MysqlDao(EntryDao):
    """
    MysqlDao is an implementation of EntryDao using MySQL as the underlying database.

    Methods:
    - __init__(self, host, user, password, database): Initializes the MysqlDao object with the MySQL connection details.
    - _create_connection(self): Creates a MySQL connection.
    - get_all_rec(self): Retrieves all records from the 'tower' table.
    - insert_new_rec(self, rec): Inserts a new record into the 'tower' table.
    - delete_rec(self, id): Deletes a record from the 'tower' table based on the given ID.
    - update_rec(self, id, update): Updates a record in the 'tower' table with the given ID and new data.
    """

    def __init__(self, host, user, password, database):
        """
        Initializes the MysqlDao object with the MySQL connection details.

        Args:
        - host (str): The hostname or IP address of the MySQL server.
        - user (str): The username to authenticate with the MySQL server.
        - password (str): The password to authenticate with the MySQL server.
        - database (str): The name of the MySQL database to connect to.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def _create_connection(self):
        """
        Creates a MySQL connection.

        Returns:
        - connection (mysql.connector.connection.MySQLConnection): The MySQL connection object.
        - None: If an error occurs while connecting to MySQL.
        """
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL")
            return None

    def get_all_rec(self):
        """
        Retrieves all records from the 'tower' table.

        Returns:
        - records (list): A list of dictionaries representing the retrieved records.
        - None: If an error occurs or the MySQL connection is not initialized.
        """
        try:
            print("Getting all updated records from the 'tower' table")
            connection = self._create_connection()
            if connection is not None:
                cursor = connection.cursor()
                select_query = "SELECT * FROM tower"
                cursor.execute(select_query)
                records = [
                    dict(zip([column[0] for column in cursor.description], row))
                    for row in cursor.fetchall()
                ]
                return records
            print("MySQL connection is not initialized..")
            return None
        finally:
            if connection is not None:
                connection.close()

    def insert_new_rec(self, rec: TWEntryRecord):
        """
        Inserts a new record into the 'tower' table.

        Args:
        - rec (TWEntryRecord): The record to be inserted.

        Returns:
        - bool: True if the record is inserted successfully, False otherwise.
        """
        print(f"Inserting new record {rec.dict()}")
        try:
            connection = self._create_connection()
            if connection is not None:
                cursor = connection.cursor()
                insert_query = "INSERT INTO tower (id, timestamp, username, description) VALUES (%(id)s, %(timestamp)s, %(username)s, %(description)s)"
                cursor.execute(insert_query, rec.dict())
                affected_ct = cursor.rowcount
                connection.commit()
                print("Record inserted successfully")
                return True
            print("MySQL connection is not initialized..")
            return False
        except Exception as e:
            print(f"Error with inserting record, record: {rec.dict()}, exception: {e}")
            return False
        finally:
            if connection is not None:
                connection.close()

    def delete_rec(self, id: str):
        """
        Deletes a record from the 'tower' table based on the given ID.

        Args:
        - id (str): The ID of the record to be deleted.

        Returns:
        - bool: True if the record is deleted successfully, False otherwise.
        """
        print(f"Deleting record with ID {id}")
        try:
            connection = self._create_connection()
            if connection is not None:
                cursor = connection.cursor()
                delete_query = "DELETE FROM tower WHERE id = %s"
                cursor.execute(delete_query, (id,))
                affected_ct = cursor.rowcount
                connection.commit()
                print(f"Deleted {affected_ct} record successfully")
                return True
            print("MySQL connection is not initialized..")
            return False
        except Exception as e:
            print(f"Error with deleting record, id: {id}, exception: {e}")
            return False
        finally:
            if connection is not None:
                connection.close()

    def update_rec(self, id: str, update: dict):
        """
        Updates a record in the 'tower' table with the given ID and new data.

        Args:
        - id (str): The ID of the record to be updated.
        - update (dict): A dictionary containing the new data to be updated.

        Returns:
        - bool: True if the record is updated successfully, False otherwise.
        """
        try:
            connection = self._create_connection()
            if connection is not None:
                cursor = connection.cursor()
                update["id"] = id
                update_query = (
                    "UPDATE tower SET "
                    + ", ".join([f"{k} = %({k})s" for k in update.keys()])
                    + " WHERE id = %(id)s"
                )
                cursor.execute(update_query, update)
                affected_ct = cursor.rowcount
                connection.commit()
                print(f"Updated {affected_ct} record successfully")
                return True
            print("MySQL connection is not initialized..")
            return False
        except Exception as e:
            print(f"Error with updating record, id: {id}, update: {update}")
            traceback.print_exc()
            return False
        finally:
            if connection is not None:
                connection.close()
