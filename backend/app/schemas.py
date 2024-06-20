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
    login: str
    phone: Optional[str]
    email: Optional[str]
    password: str
    is_admin: bool


class RecordTypeCreate(BaseModel):
    fields: List[dict] # [{title: str, type: str, for_form: bool}]


class RecordTypeUpdate(BaseModel):
    fields: List[dict] # [{title: str, type: str, for_form: bool}]


class RecordType(BaseModel):
    fields: List[dict] # [{title: str, type: str, for_form: bool}]


class RecordCreate(BaseModel):
    data: dict
    folder: str # folder id


class RecordUpdate(BaseModel):
    data: dict
    folder: str # folder id


class RecordChangeFolder(BaseModel):
    folder: str # folder id


class Page(BaseModel):
    records: List[str] # ids of records
    creator: str # creator id
    folders: List[str] # ids of records folders
