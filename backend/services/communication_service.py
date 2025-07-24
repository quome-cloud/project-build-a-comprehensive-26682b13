```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Communication
from schemas import CommunicationCreate
from typing import Optional


def create_communication(communication: CommunicationCreate, db: Session) -> Communication:
    """Creates a new communication record in the database.

    Args:
        communication: The communication data to create.
        db: The database session.

    Returns:
        The created communication record.

    Raises:
        SQLAlchemyError: If there is an error during database operations.
        ValueError: If the communication data is invalid.
    """
    try:
        db_communication = Communication(**communication.dict())
        db.add(db_communication)
        db.commit()
        db.refresh(db_communication)
        return db_communication
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError(f"Error creating communication: {e}") from e
    except ValueError as e:
        raise ValueError(f"Invalid communication data: {e}") from e


def get_communications(db: Session) -> list[Communication]:
    """Retrieves all communication records from the database.

    Args:
        db: The database session.

    Returns:
        A list of communication records.

    Raises:
        SQLAlchemyError: If there is an error during database operations.
    """
    try:
        return db.query(Communication).all()
    except SQLAlchemyError as e:
        raise SQLAlchemyError(f"Error retrieving communications: {e}") from e


def get_communication(communication_id: int, db: Session) -> Optional[Communication]:
    """Retrieves a specific communication record from the database.

    Args:
        communication_id: The ID of the communication to retrieve.
        db: The database session.

    Returns:
        The communication record, or None if not found.

    Raises:
        ValueError: If the communication_id is not a positive integer.
        SQLAlchemyError: If there is an error during database operations.
    """
    if not isinstance(communication_id, int) or communication_id <= 0:
        raise ValueError("Invalid communication ID")
    try:
        return db.query(Communication).filter(Communication.id == communication_id).first()
    except SQLAlchemyError as e:
        raise SQLAlchemyError(f"Error retrieving communication: {e}") from e
```