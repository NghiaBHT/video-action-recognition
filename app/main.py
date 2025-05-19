from fastapi import FastAPI

from app.routers import upload_file

def create_app() -> FastAPI:
    app = FastAPI(title="User Managerment")
    app.include_router(upload_file.router)
    return app

app = create_app()