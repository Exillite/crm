from app.models import User, Record, Folder, Page
from app.schemas import (
    UserRegister, UserLogin,
    RecordCreate, RecordUpdate, RecordChangeFolder,
    FolderCreate, FolderUpdate,
    PageCreate, PageUpdate
)
from typing import Optional, List
from datetime import datetime


# User services
async def create_user(user_data: UserRegister) -> User:
    new_user = User(
        login=user_data.login,
        phone=user_data.phone,
        email=user_data.email,
        password=user_data.password,
        is_admin=False
    )
    await new_user.create()
    return new_user


async def delete_user(user_id: str) -> bool:
    user = await User.get(id=user_id)
    if user:
        await user.delete()
        return True
    return False


async def get_user_by_id(user_id: str) -> Optional[User]:
    return await User.get(id=user_id)


async def get_user_by_login(login: str) -> Optional[User]:
    users = await User.find(login=login)
    if users:
        return users[0]
    return None


async def authenticate_user(user_data: UserLogin) -> Optional[User]:
    user = await get_user_by_login(user_data.login)
    if user and user.password == user_data.password:
        return user
    return None


async def list_users() -> List[User]:
    return await User.find()


# Record services
async def create_record(record_data: RecordCreate, creator_id: str) -> Record:
    new_record = Record(
        data=record_data.data,
        folder=record_data.folder,
        created_at=datetime.now(),
        update_at = datetime.now(),
        creator=creator_id
    )
    await new_record.create()
    return new_record


async def update_record(record_id: str, record_data: RecordUpdate) -> Optional[Record]:
    record = await Record.get(id=record_id)
    if record:
        record.data = record_data.data
        record.folder = record_data.folder
        record.update_at = datetime.now()
        await record.update()
        return record
    return None


async def change_record_folder(record_id: str, folder_data: RecordChangeFolder) -> Optional[Record]:
    record = await Record.get(id=record_id)
    if record:
        record.folder = folder_data.folder
        record.update_at = datetime.now()
        await record.update()
        return record
    return None


async def delete_record(record_id: str) -> bool:
    record = await Record.get(id=record_id)
    if record:
        await record.delete()
        return True
    return False


async def get_record_by_id(record_id: str) -> Optional[Record]:
    return await Record.get(id=record_id)


async def get_records_by_folder(folder_id: str) -> List[Record]:
    return await Record.find(folder=folder_id)


async def list_records() -> List[Record]:
    return await Record.find()


# Folder services
async def create_folder(folder_data: FolderCreate) -> Folder:
    new_folder = Folder(title=folder_data.title)
    await new_folder.create()
    
    page = await get_page_by_id(folder_data.page)
    if page:
        page.folders.append(new_folder.id)
        await page.update()
    
    return new_folder


async def update_folder(folder_id: str, folder_data: FolderUpdate) -> Optional[Folder]:
    folder = await Folder.get(id=folder_id)
    if folder:
        folder.title = folder_data.title
        await folder.update()
        return folder
    return None


async def delete_folder(folder_id: str) -> bool:
    folder = await Folder.get(id=folder_id)
    if folder:
        await folder.delete()
        return True
    return False


async def get_folder_by_id(folder_id: str) -> Optional[Folder]:
    return await Folder.get(id=folder_id)


async def list_folders() -> List[Folder]:
    return await Folder.find()


# Page services
async def create_page(creator_id: str, page_data: PageCreate) -> Page:
    new_page = Page(
        record_fields=page_data.record_fields,
        creator=creator_id,
        folders=[]
    )
    await new_page.create()
    return new_page


async def update_page(page_id: str, page_data: PageUpdate) -> Optional[Page]:
    page = await Page.get(id=page_id)
    if page:
        page.record_fields = page_data.record_fields
        await page.update()
        return page
    return None


async def delete_page(page_id: str) -> bool:
    page = await Page.get(id=page_id)
    if page:
        await page.delete()
        return True
    return False


async def get_page_by_id(page_id: str) -> Optional[Page]:
    return await Page.get(id=page_id)


async def list_pages() -> List[Page]:
    return await Page.find()
