```python
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class IncidentBase(BaseModel):
    """Base model for incidents."""
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10)
    location: Optional[str] = None
    status: Optional[str] = Field("open", regex="^(open|closed|resolved)$", description="Status of the incident")


class IncidentCreate(IncidentBase):
    """Model for creating new incidents."""
    pass


class IncidentUpdate(IncidentBase):
    """Model for updating existing incidents."""
    pass


class Incident(IncidentBase):
    """Model for incidents, including database ID and timestamps."""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ResourceBase(BaseModel):
    """Base model for resources."""
    type: str = Field(..., min_length=2, max_length=50)
    name: Optional[str] = None
    status: Optional[str] = Field("available", regex="^(available|unavailable|deployed)$", description="Status of the resource")
    location: Optional[str] = None


class ResourceCreate(ResourceBase):
    """Model for creating new resources."""
    pass


class ResourceUpdate(ResourceBase):
    """Model for updating existing resources."""
    pass


class Resource(ResourceBase):
    """Model for resources, including database ID and timestamps."""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CommunicationCreate(BaseModel):
    """Model for creating new communication records."""
    incident_id: int = Field(..., ge=1)
    message: str = Field(..., min_length=1, max_length=500)
    channel: str = Field(..., regex="^(email|sms|phone)$", description="Communication channel")


class Communication(BaseModel):
    """Model for communication records, including database ID and timestamps."""
    id: int
    incident_id: int
    message: str
    channel: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
```