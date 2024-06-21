from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from contextlib import asynccontextmanager

from mangodm import connect_to_mongo, close_mongo_connection

import time

from .user import router as user_router
from .record import router as record_router
from .folder import router as folder_router
from .page import router as page_router


MONGODB_CONNECTION_URL = "mongodb://crm-mongo_db-1"
DATABASE_NAME = "test_database"


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # execute when app is loading
    time.sleep(10)
    print("Loading app")
    await connect_to_mongo(MONGODB_CONNECTION_URL, DATABASE_NAME)
    print("Connected to mongo")
    yield
    # execute when app is shutting down
    print("Close db connection")
    close_mongo_connection()


app = FastAPI(lifespan=app_lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(record_router)
app.include_router(folder_router)
app.include_router(page_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
