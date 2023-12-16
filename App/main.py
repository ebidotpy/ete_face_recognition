from fastapi import FastAPI
from App.database import engine
from App import models
app = FastAPI()

models.Base.metadata.create_all(bind=engine)