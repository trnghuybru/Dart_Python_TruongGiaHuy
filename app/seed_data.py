from datetime import date
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Room

def seed_data(db: Session):
    dummy_rooms = [
        Room(tenant_name="Nguyễn Văn A", phone_number="0909123456", start_date=date(2024, 5, 1), payment_type="theo tháng"),
        Room(tenant_name="Trần Thị B", phone_number="0911222333", start_date=date(2024, 4, 15), payment_type="theo quý"),
        Room(tenant_name="Lê Văn C", phone_number="0988777666", start_date=date(2024, 1, 1), payment_type="theo năm"),
    ]

    db.add_all(dummy_rooms)
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    seed_data(db)
    print("Dữ liệu giả đã được thêm vào database!")
