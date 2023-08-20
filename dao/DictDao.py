from dao.EntryDao import EntryDao
from models.TwEntry import TWEntryRecord
from copy import copy


class DictDao(EntryDao):
    def __init__(self):
        self.data: list[TWEntryRecord] = []

    def get_all_rec(self) -> list[TWEntryRecord]:
        return self.data

    def insert_new_rec(self, rec: TWEntryRecord):
        """
        Update specific record by id, it's O(n) ops but this is just some test code
        """
        self.data.append(rec)
        return rec

    def update_rec(self, id: str, update: dict):
        """
        Update specific record by id, it's O(n) ops but this is just some test code
        """
        for i in range(len(self.data)):
            if self.data[i].id == id:
                rec = TWEntryRecord.replicate_record(self.data[i], update)
                del self.data[i]
                self.data.append(rec)
                return {"success": True, "payload": rec}
        return {"success": False, "messsage": "Unable to find id from data"}

    def delete_rec(self, id: str):
        """
        Delete specific record by id, it's O(n) ops but this is just some test code
        """
        for i in range(len(self.data)):
            if self.data[i].id == id:
                rec = copy(self.data[i])
                del self.data[i]
                return {"success": True, "deleted": rec}
        return {"success": False, "messsage": "Unable to find id from data"}
