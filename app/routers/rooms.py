from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(prefix="/rooms", tags=["Rooms"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Room)
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@router.get("/search", response_model=List[schemas.Room])
def search_rooms(
    keyword: str = Query(...),
    db: Session = Depends(get_db)
):
    return db.query(models.Room).filter(
        (models.Room.tenant_name.like(f"%{keyword}%")) |
        (models.Room.phone_number.like(f"%{keyword}%")) |
        (models.Room.id.like(f"%{keyword}%"))
    ).all()

@router.get("/", response_model=List[schemas.Room])
def get_all_rooms(db: Session = Depends(get_db)):
    return db.query(models.Room).all()

@router.delete("/{room_id}")
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room:
        db.delete(db_room)
        db.commit()
        return {"message": f"Room {room_id} deleted"}
    return {"message": f"Room {room_id} not found"}

@router.delete("/")
def delete_multiple_rooms(ids: List[int] = Query(...), db: Session = Depends(get_db)):
    deleted = db.query(models.Room).filter(models.Room.id.in_(ids)).delete(synchronize_session=False)
    db.commit()
    return {"deleted_count": deleted}
