from sqlalchemy.orm import Session

from models import Resource
from schemas import ResourceCreate, ResourceUpdate

def create_resource(resource: ResourceCreate, db: Session):
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def get_resources(db: Session):
    return db.query(Resource).all()

def get_resource(resource_id: int, db: Session):
    return db.query(Resource).filter(Resource.id == resource_id).first()

def update_resource(resource_id: int, resource: ResourceUpdate, db: Session):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if db_resource:
        for key, value in resource.dict(exclude_unset=True).items():
            setattr(db_resource, key, value)
        db.commit()
        db.refresh(db_resource)
        return db_resource
    else:
        return None

def delete_resource(resource_id: int, db: Session):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if db_resource:
        db.delete(db_resource)
        db.commit()
