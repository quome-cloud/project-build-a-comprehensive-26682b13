from sqlalchemy.orm import Session

from models import Communication
from schemas import CommunicationCreate

def create_communication(communication: CommunicationCreate, db: Session):
    db_communication = Communication(**communication.dict())
    db.add(db_communication)
    db.commit()
    db.refresh(db_communication)
    return db_communication

def get_communications(db: Session):
    return db.query(Communication).all()

def get_communication(communication_id: int, db: Session):
    return db.query(Communication).filter(Communication.id == communication_id).first()
