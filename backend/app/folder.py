from fastapi import APIRouter, Depends
from typing import Annotated

from .schemas import Folder, FolderUpdate, User
import app.services as srv

from app.user import get_current_active_user


router = APIRouter(
    prefix="/api/folder",
    responses={404: {"description": "Not found"}},
    tags=["Folder"],
)

@router.get("/{folder_id}")
async def get_folder(folder_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        folder = await srv.get_folder_by_id(folder_id)
        if folder:
            folder_response = folder.to_response()
            folder_records = await srv.get_records_by_folder(folder_id)
            records_response = [record.to_response() for record in folder_records]
            
            folder_response["records"] = records_response
            
            return folder_response
        else:
            return "Folder not found"
    except Exception as e:
        return "Error"


@router.put("/{folder_id}")
async def update_folder(folder_id: str, folder: FolderUpdate, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        updated_folder = await srv.update_folder(folder_id, folder)
        if updated_folder:
            return updated_folder.to_response()
        else:
            return "Folder not found"
    except Exception as e:
        return "Error"
