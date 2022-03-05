from fastapi import FastAPI
import polls.endpoints
from .config import Settings

app = FastAPI()
app.include_router(polls.endpoints.router, prefix="/polls")
settings = Settings()

@app.get("/")
async def root():
    return {"settings": settings}
