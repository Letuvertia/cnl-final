import os
import subprocess
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Row, Integer, String, ForeignKey,relationship

# Database connection details
DATABASE_HOST = "radius"  # Update with your FreeRadius container name or IP
DATABASE_PORT = 1812  # Update with the exposed port of the FreeRadius database
DATABASE_NAME = "locasync"  # Replace with your actual database name
DATABASE_USER = "admin"  # Replace with your database username
DATABASE_PASSWORD = "admin"  # Replace with your database password

DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(DATABASE_URI)
Base = declarative_base()
Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=False)  # Consider using a hashing mechanism
    message_history = relationship("Message", back_populates="user")

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    row_number = Column(Integer, nullable=False)
    column_number = Column(Integer, nullable=False)
    thumb_num= Row(String, nullable=False)
    value = Column(String, nullable=False)  # Using Text to store longer sentences
    user = relationship('User', back_populates='message_history')

def execute_sql_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as sql_file:
            sql_script = sql_file.read()
            subprocess.run(['mysql', '-h', DATABASE_HOST, '-P', str(DATABASE_PORT), '-u', DATABASE_USER, '-p', DATABASE_PASSWORD], input=sql_script.encode(), check=True)
    else:
        print(f"Schema file {filepath} not found. Skipping import.")


if __name__ == "__main__":
    # Check and potentially import schema.sql
    # execute_sql_file("db/schema.sql")
    pass