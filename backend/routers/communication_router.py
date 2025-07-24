from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import CommunicationCreate, Communication
from services import communication_service

router = APIRouter(prefix="/api/communications", tags=["Communications"])

@router.post("", status_code=status.HTTP_201_CREATED, response_model=Communication)
def create_communication(communication: CommunicationCreate, db: Session = Depends(get_db)):
    return communication_service.create_communication(communication, db)

@router.get("", response_model=list[Communication])
def get_communications(db: Session = Depends(get_db)):
    return communication_service.get_communications(db)

@router.get("/{communication_id}", response_model=Communication)
def get_communication(communication_id: int, db: Session = Depends(get_db)):
    communication = communication_service.get_communication(communication_id, db)
    if not communication:
        raise HTTPException(status_code=404, detail="Communication not found")
    return communication
