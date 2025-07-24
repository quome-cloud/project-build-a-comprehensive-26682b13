from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import ResourceCreate, Resource, ResourceUpdate
from services import resource_service

router = APIRouter(prefix="/api/resources", tags=["Resources"])

@router.post("", status_code=status.HTTP_201_CREATED, response_model=Resource)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    return resource_service.create_resource(resource, db)

@router.get("", response_model=list[Resource])
def get_resources(db: Session = Depends(get_db)):
    return resource_service.get_resources(db)

@router.get("/{resource_id}", response_model=Resource)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resource_service.get_resource(resource_id, db)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@router.put("/{resource_id}", response_model=Resource)
def update_resource(resource_id: int, resource: ResourceUpdate, db: Session = Depends(get_db)):
    db_resource = resource_service.get_resource(resource_id, db)
    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource_service.update_resource(resource_id, resource, db)

@router.delete("/{resource_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    resource_service.delete_resource(resource_id, db)
