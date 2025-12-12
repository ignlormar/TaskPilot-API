from fastapi import FastAPI
from app.database import engine
from app.models import base

app = FastAPI()

base.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a TaskPilot"}