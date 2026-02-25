import os
from sqlalchemy import create_engine


def get_engine():
    """
    Create a SQLAlchemy engine using a DATABASE_URL env var.
    Example:
      postgresql+psycopg2://user:password@localhost:5432/monkey_analytics
    """
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL env var is not set.")
    return create_engine(db_url)