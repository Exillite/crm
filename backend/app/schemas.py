from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserRegister(BaseModel):
    login: str
    phone: Optional[str]
    email: Optional[str]
    password: str


class UserLogin(BaseModel):
    login: str
    password: str


class User(BaseModel):
    id: str
    login: str
    phone: Optional[str]
    email: Optional[str]
    is_admin: bool


class RecordCreate(BaseModel):
    data: dict
    folder: str # folder id

class RecordUpdate(BaseModel):
    data: dict
    folder: str # folder id


class RecordChangeFolder(BaseModel):
    folder: str # folder id


class FolderCreate(BaseModel):
    title: str
    page: str


class FolderUpdate(BaseModel):
    title: str


class Folder(BaseModel):
    title: str


class PageCreate(BaseModel):
    record_fields: List[dict]


class PageUpdate(BaseModel):
    record_fields: List[dict]


class Page(BaseModel):
    record_fields: List[dict]
    creator: str # creator id
    folders: List[str] # ids of records folders
