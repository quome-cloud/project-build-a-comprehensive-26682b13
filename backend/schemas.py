from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class IncidentCreate(BaseModel):
    title: str
    description: str
    location: Optional[str] = None
    status: Optional[str] = "open"

class IncidentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None

class Incident(BaseModel):
    id: int
    title: str
    description: str
    location: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ResourceCreate(BaseModel):
    type: str
    name: Optional[str] = None
    status: Optional[str] = "available"
    location: Optional[str] = None

class ResourceUpdate(BaseModel):
    type: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None

class Resource(BaseModel):
    id: int
    type: str
    name: Optional[str] = None
    status: str
    location: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CommunicationCreate(BaseModel):
    incident_id: int
    message: str
    channel: str

class Communication(BaseModel):
    id: int
    incident_id: int
    message: str
    channel: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
