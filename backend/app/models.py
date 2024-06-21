from mangodm import Document
from typing import List, Optional
from datetime import datetime


class User(Document):
    login: str
    phone: Optional[str]
    email: Optional[str]
    password: str
    is_admin: bool
    
    class Config:
        collection_name = "Users"


class RecordType(Document):
    fields: List[dict] # [{title: str, type: str, for_form: bool}]
    
    class Config:
        collection_name = "RecordTypes"


class Record(Document):
    data: dict
    folder: str # folder id
    created_at: datetime
    update_at: datetime
    creator: str # creator id

    class Config:
        collection_name = "Records"


class Folder(Document):
    title: str

    class Config:
        collection_name = "Folders"


class Page(Document):
    record_fields: List[dict] # [{title: str, type: str, for_form: bool}]
    creator: str # creator id
    folders: List[str] # ids of records folders


User.register_collection()
RecordType.register_collection()
Record.register_collection()
Folder.register_collection()
Page.register_collection()
