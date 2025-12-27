from fastapi import FastAPI

app = FastAPI(title="Hibiki Engine")


@app.get("/")
async def root():
    return {"message": "Hello from hibiki-engine!"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
