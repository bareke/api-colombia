from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.settings.database import database
from app.settings.environment import settings
from app.settings.routers import routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

prefix = "/api"

# Register all routers
[app.include_router(router, prefix=prefix) for router in routers]

if __name__ == "__main__":
    port = settings.get("app").get("port")
    uvicorn.run(app, host="0.0.0.0", port=port)
