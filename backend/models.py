```python
import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Incident(Base):
    """Represents an emergency incident."""
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(255))
    status = Column(String(50))
    created_at = Column(DateTime, default=func.now(), server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class Resource(Base):
    """Represents an emergency resource."""
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(255), nullable=False)
    name = Column(String(255))
    status = Column(String(50))
    location = Column(String(255))
    created_at = Column(DateTime, default=func.now(), server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class Communication(Base):
    """Represents a communication record related to an incident."""
    __tablename__ = "communications"
    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("incidents.id"))
    communication_text = Column(Text, nullable=False)
    channel = Column(String(50))
    created_at = Column(DateTime, default=func.now(), server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    incident = relationship("Incident")
```