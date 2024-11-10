from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from uuid import uuid4
import uvicorn
from sqlalchemy.orm import Session

from db import SessionLocal
import crud

app = FastAPI()

class ToDoList(BaseModel):
    id: str
    title: str
    description: str = None
    complete: bool


def getdb():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


@app.get("/task", response_model=List[ToDoList])
def get_all_tasks(db: Session = Depends(getdb)):
    task = crud.get_all_tasks(db)
    return task

@app.post("/task", response_model=ToDoList)
def add_task(title: str, description: Optional[str]=None, db: Session = Depends(getdb)):
    newtask = crud.add_task(db, title, description)
    return newtask

@app.get("/task/{taskid}", response_model=ToDoList)
def get_task(taskid: str, db: Session = Depends(getdb)):
    task = crud.get_task(db, taskid)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/task/{taskid}", response_model=ToDoList)
def update_task(taskid: str, title: Optional[str]=None, description: Optional[str]=None, complete: Optional[bool]=None, db: Session = Depends(getdb)):
    task = crud.update_task(db, taskid, title, description, complete)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/task/{taskid}")
def delete_task(taskid: str, db: Session = Depends(getdb)):
    task = crud.remove_task(db, taskid)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)