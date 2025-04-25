from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    tenant_name = Column(String, index=True)
    phone_number = Column(String, index=True)
    start_date = Column(Date)
    payment_type = Column(String)  # theo tháng, quý, năm
