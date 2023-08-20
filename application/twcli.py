from dao.MySQLDao import MysqlDao
from dao.EntryDao import EntryDao
from models.TwEntry import TWEntryRecord
import yaml

import sys
import argparse

from util.metrics import calculate_elapsed_time

# Load configurations from the config file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


dao: EntryDao = MysqlDao(
    host=config["Database"]["host"],
    user=config["Database"]["user"],
    password=config["Database"]["password"],
    database=config["Database"]["database"],
)


@calculate_elapsed_time
def handle_get_all():
    response = dao.get_all_rec()
    print(response)
    return True


@calculate_elapsed_time
def handle_insert(username: str, description: str):
    if not username or not description:
        print(
            "--username and --description are required to process with insert request"
        )
        return False
    rec = TWEntryRecord.create_entry(username, description)
    response = dao.insert_new_rec(rec)
    print(response)
    return True


@calculate_elapsed_time
def handle_update(id: str, username: str, description: str):
    if not id:
        print("ID is required to process with delete request")
        return False

    if not username and not description:
        print(
            "At least --username or --description is required to process with update request"
        )
        return False

    update = {}
    if username:
        update["username"] = username

    if description:
        update["description"] = description

    success = dao.update_rec(id, update)

    if not success:
        return False

    response = dao.get_all_rec()
    print(response)
    return True


@calculate_elapsed_time
def handle_delete(id: str):
    """
    Handling delete request
    """
    if not id:
        print("ID is required to process with delete request")
        return False
    success = dao.delete_rec(id)
    if not success:
        return False
    response = dao.get_all_rec()
    print(response)
    return True


def main():
    parser = argparse.ArgumentParser(description="CLI to do CRUD on tower table")

    # Add arguments
    parser.add_argument("--username", type=str, help="Username")
    parser.add_argument("--description", type=str, help="Description of the entry")
    parser.add_argument("--id", type=str, help="id")
    parser.add_argument(
        "--action",
        choices=["get", "delete", "update", "insert"],
        help="Specify the action",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Access the argument values
    id = args.id
    username = args.username
    description = args.description
    action = args.action

    # Perform action based on the selected action
    if action == "get":
        success = handle_get_all()
        if not success:
            sys.exit(1)
    elif action == "delete":
        success = handle_delete(id)
        if not success:
            sys.exit(1)
    elif action == "update":
        success = handle_update(id, username, description)
        if not success:
            sys.exit(1)
    elif action == "insert":
        success = handle_insert(username, description)
        if not success:
            sys.exit(1)
    else:
        print("Invalid action specified.")
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
