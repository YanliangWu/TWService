import unittest
from unittest.mock import MagicMock
from models.TwEntry import TWEntryRecord
from dao.MySQLDao import MysqlDao


class MysqlDaoTest(unittest.TestCase):

    def setUp(self):
        self.host = 'localhost'
        self.user = 'myuser'
        self.password = 'mypassword'
        self.database = 'mydatabase'
        self.dao = MysqlDao(self.host, self.user, self.password, self.database)

    def tearDown(self):
        pass

    def test_get_all_rec(self):
        # Mock the _create_connection method to return a mock connection and cursor
        connection_mock = MagicMock()
        cursor_mock = MagicMock()
        connection_mock.cursor.return_value = cursor_mock
        self.dao._create_connection = MagicMock(return_value=connection_mock)

        # Mock the fetchall method of the cursor to return a sample list of records
        records = [{'id': 1, 'timestamp': '2023-08-20', 'username': 'john', 'description': 'Sample record'}]
        cursor_mock.fetchall.return_value = [(1, '2023-08-20', 'john', 'Sample record')]
        cursor_mock.description = [('id',), ('timestamp',), ('username',), ('description',)]  # Mocked cursor.description

        # Call the method under test
        result = self.dao.get_all_rec()

        # Assertions
        self.assertEqual(result, records)
        self.dao._create_connection.assert_called_once()
        cursor_mock.execute.assert_called_once_with("SELECT * FROM tower")
        cursor_mock.fetchall.assert_called_once()
        connection_mock.close.assert_called_once()

    def test_insert_new_rec(self):
        # Mock the _create_connection method to return a mock connection and cursor
        connection_mock = MagicMock()
        cursor_mock = MagicMock()
        connection_mock.cursor.return_value = cursor_mock
        self.dao._create_connection = MagicMock(return_value=connection_mock)

        # Call the method under test
        rec = TWEntryRecord(id=1, timestamp='2023-08-20', username='john', description='Sample record')
        result = self.dao.insert_new_rec(rec)

        # Assertions
        self.assertTrue(result)
        self.dao._create_connection.assert_called_once()
        cursor_mock.execute.assert_called_once()
        connection_mock.commit.assert_called_once()
        connection_mock.close.assert_called_once()

    def test_delete_rec(self):
        # Mock the _create_connection method to return a mock connection and cursor
        connection_mock = MagicMock()
        cursor_mock = MagicMock()
        connection_mock.cursor.return_value = cursor_mock
        self.dao._create_connection = MagicMock(return_value=connection_mock)

        # Call the method under test
        id = '1'
        result = self.dao.delete_rec(id)

        # Assertions
        self.assertTrue(result)
        self.dao._create_connection.assert_called_once()
        cursor_mock.execute.assert_called_once_with("DELETE FROM tower WHERE id = %s", (id,))
        connection_mock.commit.assert_called_once()
        connection_mock.close.assert_called_once()

    def test_update_rec(self):
        # Mock the _create_connection method to return a mock connection and cursor
        connection_mock = MagicMock()
        cursor_mock = MagicMock()
        connection_mock.cursor.return_value = cursor_mock
        self.dao._create_connection = MagicMock(return_value=connection_mock)

        # Call the method under test
        id = '1'
        update = {'username': 'jane'}
        result = self.dao.update_rec(id, update)

        # Assertions
        self.assertTrue(result)
        self.dao._create_connection.assert_called_once()
        cursor_mock.execute.assert_called_once()
        connection_mock.commit.assert_called_once()
        connection_mock.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()