from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.database import Base, engine
from app.routers import tasks, health

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Cria as tabelas ao arrancar
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Task Manager API — DevOps Portfolio Project",
    lifespan=lifespan
)

app.include_router(health.router)
app.include_router(tasks.router) 