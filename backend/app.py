from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.base import get_db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/db/health-check")
async def db_health_check(session: AsyncSession = Depends(get_db)):
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "details": str(e)}