from fastapi import APIRouter, Depends
from typing import Annotated

from .schemas import User, RecordCreate, RecordUpdate
import app.services as srv

from app.user import get_current_active_user


router = APIRouter(
    prefix="/api/record",
    responses={404: {"description": "Not found"}},
    tags=["Record"],
)


@router.post("/")
async def create_record(record: RecordCreate, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        new_record = await srv.create_record(record, current_user.id)
        return new_record.to_response()
    except Exception as e:
        return "Error"


@router.get("/{record_id}")
async def get_record(record_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        record = await srv.get_record_by_id(record_id)
        if record:
            return record.to_response()
        else:
            return "Record not found"
    except Exception as e:
        return "Error"


@router.put("/{record_id}")
async def update_record(record_id: str, record: RecordUpdate, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        updated_record = await srv.update_record(record_id, record)
        if updated_record:
            return updated_record.to_response()
        else:
            return "Record not found"
    except Exception as e:
        return "Error"


@router.delete("/{record_id}")
async def delete_record(record_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    try:
        deleted_record = await srv.delete_record(record_id)
        if deleted_record:
            return "OK"
        else:
            return "Record not found"
    except Exception as e:
        return "Error"
