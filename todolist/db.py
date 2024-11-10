from typing import Optional

from sqlalchemy import create_engine, String, Boolean, Column
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column

engine = create_engine("sqlite:///./tasks.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    complete = Column(Boolean, default=False)

Base.metadata.create_all(engine)