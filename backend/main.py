from app.routes.health import router as health_router
from fastapi import FastAPI

app = FastAPI(
    title="Instant Dev Environment Generator",
    version="0.1.0",
)
app.include_router(health_router)


@app.get("/", tags=["root"])
def read_root():
    return {"message": "IDG API is alive!"}
