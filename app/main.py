from fastapi import FastAPI
from app.routes import api1, api2
from app.models import Base
from app.database import engine

app = FastAPI(title="KPA Backend APIs")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(api1.router)
app.include_router(api2.router)
