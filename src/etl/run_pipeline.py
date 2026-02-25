from sqlalchemy import text
from src.db.connection import get_engine


def main():
    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("DB connection OK")


if __name__ == "__main__":
    main()