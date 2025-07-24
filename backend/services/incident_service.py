from sqlalchemy.orm import Session

from models import Incident
from schemas import IncidentCreate, IncidentUpdate

def create_incident(incident: IncidentCreate, db: Session):
    db_incident = Incident(**incident.dict())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

def get_incidents(db: Session):
    return db.query(Incident).all()

def get_incident(incident_id: int, db: Session):
    return db.query(Incident).filter(Incident.id == incident_id).first()

def update_incident(incident_id: int, incident: IncidentUpdate, db: Session):
    db_incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if db_incident:
        for key, value in incident.dict(exclude_unset=True).items():
            setattr(db_incident, key, value)
        db.commit()
        db.refresh(db_incident)
        return db_incident
    else:
        return None

def delete_incident(incident_id: int, db: Session):
    db_incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if db_incident:
        db.delete(db_incident)
        db.commit()
