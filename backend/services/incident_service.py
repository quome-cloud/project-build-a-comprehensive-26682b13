```python
from sqlalchemy.orm import Session
from sqlalchemy import exc

from models import Incident
from schemas import IncidentCreate, IncidentUpdate
from typing import Optional


def create_incident(incident: IncidentCreate, db: Session) -> Incident:
    """Creates a new incident.

    Args:
        incident: The incident data to create.
        db: The database session.

    Returns:
        The created incident.

    Raises:
        exc.SQLAlchemyError: If there's an error during database operations.
        ValueError: If input data is invalid.
    """
    if not incident.title or not incident.description:
        raise ValueError("Incident title and description are required.")

    db_incident = Incident(**incident.dict())
    try:
        db.add(db_incident)
        db.commit()
        db.refresh(db_incident)
        return db_incident
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise exc.SQLAlchemyError(f"Error creating incident: {e}") from e


def get_incidents(db: Session) -> list[Incident]:
    """Retrieves all incidents.

    Args:
        db: The database session.

    Returns:
        A list of incidents.
    """
    return db.query(Incident).all()


def get_incident(incident_id: int, db: Session) -> Optional[Incident]:
    """Retrieves an incident by ID.

    Args:
        incident_id: The ID of the incident.
        db: The database session.

    Returns:
        The incident if found, otherwise None.
    """
    return db.query(Incident).filter(Incident.id == incident_id).first()


def update_incident(incident_id: int, incident: IncidentUpdate, db: Session) -> Optional[Incident]:
    """Updates an incident.

    Args:
        incident_id: The ID of the incident to update.
        incident: The updated incident data.
        db: The database session.

    Returns:
        The updated incident if found, otherwise None.

    Raises:
        exc.SQLAlchemyError: If there's an error during database operations.
    """
    try:
        db_incident = db.query(Incident).filter(Incident.id == incident_id).first()
        if db_incident:
            for key, value in incident.dict(exclude_unset=True).items():
                setattr(db_incident, key, value)
            db.commit()
            db.refresh(db_incident)
            return db_incident
        else:
            return None
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise exc.SQLAlchemyError(f"Error updating incident: {e}") from e


def delete_incident(incident_id: int, db: Session) -> None:
    """Deletes an incident.

    Args:
        incident_id: The ID of the incident to delete.
        db: The database session.

    Raises:
        exc.SQLAlchemyError: If there's an error during database operations.
    """
    try:
        db_incident = db.query(Incident).filter(Incident.id == incident_id).first()
        if db_incident:
            db.delete(db_incident)
            db.commit()
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise exc.SQLAlchemyError(f"Error deleting incident: {e}") from e
```