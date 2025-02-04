from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models import Film
from schemas import FilmCreate, FilmRead
from database import get_db

router = APIRouter()

@router.get("/movies/")
def read_movies():
    return {"message": "List of movies"}

@router.get("/movies/{film_id}", response_model=FilmRead)
def get_film(film_id: int, db: Session = Depends(get_db)):
    film = db.query(Film).filter(Film.id == film_id).first()
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

@router.post("/movies/", response_model=FilmRead)
def create_film(film: FilmCreate, db: Session = Depends(get_db)):
    new_film = Film(**film.dict())
    db.add(new_film)
    db.commit()
    db.refresh(new_film)
    return new_film
