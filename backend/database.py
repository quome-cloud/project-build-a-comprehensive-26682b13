```python
import os
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from typing import Generator

from models import Base

# Configuration section
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./emergency_management.db')


def get_db() -> Generator[sessionmaker, None, None]:
    """Provides a database session using a context manager.

    This function creates a database engine, a sessionmaker, and yields a database session.
    The session is automatically closed when exiting the `with` block.

    Returns:
        Generator[sessionmaker, None, None]: A generator yielding a database session.

    Raises:
        Exception: If there's an issue creating the database engine or the database.
    """
    try:
        engine = create_engine(
            DATABASE_URL,
            connect_args={'check_same_thread': False},
            echo=True  # For debugging purposes, remove in production
        )
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)
        yield SessionLocal
    except exc.SQLAlchemyError as e:
        print(f"Database error: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
    finally:
        # Ensure the engine is disposed of to prevent resource leaks
        engine.dispose()

```