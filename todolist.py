from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
import uvicorn

app = FastAPI()

class ToDoList(BaseModel):
    id: str
    title: str
    description: str
    completed: bool

taskdb = []


@app.get("/task", response_model=List[ToDoList])
def get_all_tasks():
    return taskdb

@app.post("/task", response_model=ToDoList)
def add_task(title: str, description: Optional[str]=None):
    newtask = ToDoList(id=str(uuid4()), title=title, description=description, completed=False)
    taskdb.append(newtask)
    return newtask

@app.get("/task/{taskid}", response_model=ToDoList)
def get_task(id: str):
    got_task = next((get_task for get_task in taskdb if get_task.id == id), None)
    if got_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return got_task

@app.post("/task/{taskid}", response_model=ToDoList)
def update_task(id: str, title: Optional[str]=None, description: Optional[str]=None, completed: Optional[bool]=None):
    updated_task = next((update_task for update_task in taskdb if update_task.id == id), None)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if title is not None:
        updated_task.title = title
    if description is not None:
        updated_task.description = description
    if completed is not None:
        updated_task.completed = completed
    return updated_task

@app.delete("/task/{taskid}")
def delete_task(id: str):
    global taskdb
    taskdb = [task for task in taskdb if task.id != id]
    return {"detail":"Task deleted"}

if __name__ == '__main__':
    uvicorn.run('todolist:app', reload=True)