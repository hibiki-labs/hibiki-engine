from fastapi import FastAPI
from routers import chat

app = FastAPI(title="Hibiki Engine")

app.include_router(router=chat.router, prefix="/chat", tags=["chat"])


@app.get("/")
async def root():
    return {"message": "Hello from hibiki-engine!"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
