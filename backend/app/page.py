from fastapi import APIRouter, Depends
from typing import Annotated

from .schemas import Page, PageCreate, PageUpdate, User, FolderCreate
import app.services as srv

from app.user import get_current_active_user


router = APIRouter(
    prefix="/api/page",
    responses={404: {"description": "Not found"}},
    tags=["Page"],
)

@router.post("/")
async def create_page(page: PageCreate, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        new_page = await srv.create_page(current_user.id, page)
        return new_page.to_response()
    except Exception as e:
        return "Error"
    
@router.get("/{page_id}")
async def get_page(page_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        page = await srv.get_page_by_id(page_id)
        if page:
            return page.to_response()
        else:
            return "Page not found"
    except Exception as e:
        return "Error"


@router.put("/{page_id}")
async def update_page(page_id: str, page: PageUpdate, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        updated_page = await srv.update_page(page_id, page)
        if updated_page:
            return updated_page.to_response()
        else:
            return "Page not found"
    except Exception as e:
        return "Error"

@router.post("/{page_id}/folder")
async def create_folder(page_id: str, folder: FolderCreate, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        new_folder = await srv.create_folder(folder)
        if new_folder:
            return new_folder.to_response()
        else:
            return "Page not found"
    except Exception as e:
        return "Error"
