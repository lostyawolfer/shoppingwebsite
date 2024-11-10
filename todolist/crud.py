from sqlalchemy.orm import Session
from uuid import uuid4
from db import Task

def get_all_tasks(db: Session):
    return db.query(Task).all()

def add_task(db: Session, title: str, description: str=None):
    newtask = Task(id=str(uuid4()), title=title, description=description, complete=False)
    db.add(newtask)
    db.commit()
    db.refresh(newtask)
    return newtask

def get_task(db: Session, taskid: str):
    return db.query(Task).filter(Task.id == taskid).first()

def remove_task(db: Session, taskid: str):
    task = db.query(Task).filter(Task.id == taskid).first()
    if task is None:
        return None
    db.delete(task)
    db.commit()
    return task

def update_task(db: Session, taskid: str, title: str=None, description: str=None, complete: bool=None):
    task = db.query(Task).filter(Task.id == taskid).first()
    if task is None:
        return None

    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if complete is not None:
        task.complete = complete

    db.commit()
    db.refresh(task)
    return task