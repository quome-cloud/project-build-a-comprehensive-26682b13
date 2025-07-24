from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import IncidentCreate, Incident, IncidentUpdate
from services import incident_service

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])

@router.post("", status_code=status.HTTP_201_CREATED, response_model=Incident)
def create_incident(incident: IncidentCreate, db: Session = Depends(get_db)):
    return incident_service.create_incident(incident, db)

@router.get("", response_model=list[Incident])
def get_incidents(db: Session = Depends(get_db)):
    return incident_service.get_incidents(db)

@router.get("/{incident_id}", response_model=Incident)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = incident_service.get_incident(incident_id, db)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.put("/{incident_id}", response_model=Incident)
def update_incident(incident_id: int, incident: IncidentUpdate, db: Session = Depends(get_db)):
    db_incident = incident_service.get_incident(incident_id, db)
    if not db_incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident_service.update_incident(incident_id, incident, db)

@router.delete("/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    incident_service.delete_incident(incident_id, db)
