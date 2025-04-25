from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class RoomBase(BaseModel):
    tenant_name: str
    phone_number: str
    start_date: date
    payment_type: str

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: int

    class Config:
        orm_mode = True
