from fastapi import FastAPI

from .database import Base, engine
from .routers import auth, doctors, patients


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Doctor Patient Management API",
    description="End-to-End FastAPI Backend Application",
    version="1.0.0"
)


app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(patients.router)


@app.get("/")
def root():
    return {
        "message": "Doctor Patient Management API is running"
    }
