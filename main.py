from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.settings.database import connect_db, disconnect_db
from app.settings.environment import settings
from app.settings.modules import routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()


app = FastAPI(lifespan=lifespan)

prefix = "/api/v1"

# Register all routers
[app.include_router(router, prefix=prefix) for router in routers]

if __name__ == "__main__":
    port = settings.get("app").get("port")
    uvicorn.run(app, host="0.0.0.0", port=port)
