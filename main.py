from fastapi import FastAPI
from routers import users, movies
from database import engine
from models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(movies.router)
