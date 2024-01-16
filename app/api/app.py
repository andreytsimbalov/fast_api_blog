from contextlib import asynccontextmanager

from fastapi import FastAPI
from api.endpoints import root
from api.endpoints import admin


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Start '{app.title}'")
    yield
    print(f"End '{app.title}'")


app = FastAPI(
    title='FastApi Blog',
    version='0.0.2',
    lifespan=lifespan
)
app.include_router(root.router)
app.include_router(admin.router)
