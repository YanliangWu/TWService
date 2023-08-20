
from dao.MySQLDao import MysqlDao
from dao.EntryDao import EntryDao
from models.TwEntry import TWEntryRecord

import argparse

dao:EntryDao = MysqlDao(host="localhost", user="root", password="123456", database="towerdb")

def handle_get_all():
    response = dao.get_all_rec()
    print(response)
    return 0

def handle_insert(username: str, description: str):
    if not username or not description: 
        print("--username and --description are required to process with insert request")
        return 1
    rec = TWEntryRecord.create_entry(username, description)
    response = dao.insert_new_rec(rec)
    print(response)
    return 0

def handle_update(id: str, username: str, description: str): 
    if not id: 
        print("ID is required to process with delete request")
        return 1
    
    if not username and not description: 
        print("At least --username or --description is required to process with update request")
        return 1
    
    result = dao.delete_rec(id)
    if not result.get("success"):
        print(f"Failed to execute delete request, message: {result.get('messsage')}")
        return 1
    
    print(f"Successfully Executed, {result}")
    return 0

def handle_delete(id: str): 
    """
    Handling delete request
    """

    id = ""
    if not id: 
        print("ID is required to process with delete request")
        return 1
    
    result = dao.delete_rec(id)
    if not result.get("success"):
        print(f"Failed to execute delete request, message: {result.get('messsage')}")
        return 1
    
    print(f"Successfully Executed, {result}")
    return 0

def main():
    parser = argparse.ArgumentParser(description='CLI to do CRUD on tower table')
    
    # Add arguments
    parser.add_argument('--name', type=str, help='Specify the name')
    parser.add_argument('--description', type=str, help='Specify the description')
    parser.add_argument('--action', choices=['get', 'delete', 'update', 'insert'], help='Specify the action')

    # Parse the arguments
    args = parser.parse_args()

    # Access the argument values
    name = args.name
    description = args.description
    action = args.action

    # Perform action based on the selected action
    if action == 'get':
        # Add your get logic here
        handle_get_all()
    elif action == 'delete':
        print(f'Performing DELETE action with name: {name} and description: {description}')
        # Add your delete logic here
    elif action == 'update':
        print(f'Performing UPDATE action with name: {name} and description: {description}')
        # Add your update logic here
    elif action == 'insert':
        print(f'Performing INSERT action with name: {name} and description: {description}')
        # Add your insert logic here
        handle_insert(name, description)
    else:
        print('Invalid action specified.')

if __name__ == '__main__':
    main()
