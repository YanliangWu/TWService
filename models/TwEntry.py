from dataclasses import dataclass, asdict
from uuid import uuid4 as new_uuid
import time

USERNAME = "username"
DESCRIPTION = "description"

@dataclass
class TWEntryRecord:
    id: str
    timestamp: str
    username: str
    description: str

    @classmethod
    def from_dict(cls, d: dict) -> "TWEntryRecord":
        return cls(id=d.get("id"), timestamp=time.time(), username=d.get("username"), description=d.get("description"))

    @classmethod
    def create_entry(cls, d: dict) -> "TWEntryRecord":
        return cls(id=str(new_uuid()), timestamp=time.time(), username=d.get("username"), description=d.get("description"))
    
    @classmethod
    def replicate_record(cls, existed: "TWEntryRecord", replace: dict):
        return cls(id=existed.id, timestamp=time.time(), username=replace.get("username") or existed.username, description=replace.get("description") or existed.description)

    dict = asdict
