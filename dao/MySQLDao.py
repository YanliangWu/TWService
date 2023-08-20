
from dao.EntryDao import EntryDao
from models.TwEntry import TWEntryRecord

import mysql.connector

class MysqlDao(EntryDao):
    """
    MysqlEntryDao is an implementation of EntryDao using MySQL as the underlying database.
    """

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def _create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL")
            return None 

    def get_all_rec(self):
        try:
            print("Getting all records from tower db")
            connection = self._create_connection()
            if connection is not None:
                cursor = connection.cursor()
                select_query = "SELECT * FROM tower"
                cursor.execute(select_query)
                records = cursor.fetchall()
                return records
        finally:
            if connection is not None:
                connection.close()

    def insert_new_rec(self, rec: TWEntryRecord):
        try:
            connection = self._create_connection()
            if connection is not None:
                cursor = connection.cursor()
                insert_query = "INSERT INTO tower (id, timestamp, username, description) VALUES (%(id)s, %(timestamp)s, %(username)s, %(description)s)"
                cursor.execute(insert_query, rec.dict())
                connection.commit()
                print("Record inserted successfully")
        finally:
            if connection is not None:
                connection.close()

    def delete_rec(self, id: str):
        try:
            connection = self._create_connection()
            if connection is not None:
                cursor = connection.cursor()
                delete_query = "DELETE FROM tower WHERE id = %s"
                cursor.execute(delete_query, (id,))
                connection.commit()
                print("Record deleted successfully")
        finally:
            if connection is not None:
                connection.close()

    def update_rec(self, id: str, update: dict):
        
        try:
            connection = self._create_connection()
            if connection is not None:
                cursor = connection.cursor()
                update_query = "UPDATE tower SET timestamp = %s, username = %s, description = %s WHERE id = %s"
                cursor.execute(update_query, (update["timestamp"], update["username"], update["description"], id))
                connection.commit()
                print("Record updated successfully")
        finally:
            if connection is not None:
                connection.close()