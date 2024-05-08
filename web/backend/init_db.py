import os
import subprocess

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Database connection details
DATABASE_HOST = "radius"  # Update with your FreeRadius container name or IP
DATABASE_PORT = 1812  # Update with the exposed port of the FreeRadius database
DATABASE_NAME = "locasync"  # Replace with your actual database name
DATABASE_USER = "admin"  # Replace with your database username
DATABASE_PASSWORD = "admin"  # Replace with your database password

DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(DATABASE_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=False)  # Consider using a hashing mechanism


def execute_sql_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as sql_file:
            sql_script = sql_file.read()
            subprocess.run(['mysql', '-h', DATABASE_HOST, '-P', str(DATABASE_PORT), '-u', DATABASE_USER, '-p', DATABASE_PASSWORD], input=sql_script.encode(), check=True)
    else:
        print(f"Schema file {filepath} not found. Skipping import.")


Base.metadata.create_all(engine)

# Check and potentially import schema.sql
execute_sql_file("db/schema.sql")

if __name__ == "__main__":
    # Example usage (replace with your logic)
    # ... (create users, etc.)
    pass
