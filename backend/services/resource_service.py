```python
from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models import Resource
from schemas import ResourceCreate, ResourceUpdate


def create_resource(resource: ResourceCreate, db: Session) -> Resource:
    """Creates a new resource.

    Args:
        resource: The resource data to create.
        db: The database session.

    Returns:
        The created resource.

    Raises:
        SQLAlchemyError: If a database error occurs.
        ValueError: If input data is invalid.
    """
    if not resource.name or not resource.type:
        raise ValueError("Resource name and type are required.")

    try:
        db_resource = Resource(**resource.dict())
        db.add(db_resource)
        db.commit()
        db.refresh(db_resource)
        return db_resource
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError(f"Database error creating resource: {e}") from e


def get_resources(db: Session) -> list[Resource]:
    """Retrieves all resources.

    Args:
        db: The database session.

    Returns:
        A list of all resources.

    Raises:
        SQLAlchemyError: If a database error occurs.
    """
    try:
        return db.query(Resource).all()
    except SQLAlchemyError as e:
        raise SQLAlchemyError(f"Database error retrieving resources: {e}") from e


def get_resource_by_id(resource_id: int, db: Session) -> Optional[Resource]:
    """Retrieves a resource by ID.

    Args:
        resource_id: The ID of the resource.
        db: The database session.

    Returns:
        The resource if found, otherwise None.

    Raises:
        SQLAlchemyError: If a database error occurs.
    """
    try:
        return db.query(Resource).filter(Resource.id == resource_id).first()
    except SQLAlchemyError as e:
        raise SQLAlchemyError(f"Database error retrieving resource: {e}") from e


def update_resource(resource_id: int, resource: ResourceUpdate, db: Session) -> Optional[Resource]:
    """Updates a resource.

    Args:
        resource_id: The ID of the resource to update.
        resource: The updated resource data.
        db: The database session.

    Returns:
        The updated resource if found, otherwise None.

    Raises:
        SQLAlchemyError: If a database error occurs.
    """
    try:
        db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if db_resource:
            updates = resource.dict(exclude_unset=True)
            db.query(Resource).filter(Resource.id == resource_id).update(updates)
            db.commit()
            return db.query(Resource).get(resource_id)
        else:
            return None
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError(f"Database error updating resource: {e}") from e


def delete_resource(resource_id: int, db: Session) -> None:
    """Deletes a resource.

    Args:
        resource_id: The ID of the resource to delete.
        db: The database session.

    Raises:
        SQLAlchemyError: If a database error occurs.
    """
    try:
        db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if db_resource:
            db.delete(db_resource)
            db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError(f"Database error deleting resource: {e}") from e
```