from fastapi import HTTPException
from src.dtos import reqBody
from src.models.model import Todo
# //This is a dictionary u shd access it like a array
data = [
    {"id":1, "name":"Rupesh1", "sex":"Male"},
    {"id":2, "name":"Rupesh2", "sex":"Male"},
    {"id":3, "name":"Rupesh3", "sex":"Male"},
    {"id":4, "name":"Rupesh4", "sex":"Male"},
    {"id":5, "name":"Rupesh5", "sex":"Male"},
    {"id":6, "name":"Rupesh6", "sex":"Male"}
]


def todoget():
    return data

def posttogetParams(todoId:int | None = None):
    if todoId:
        for todos in data:
            if todos["id"] == todoId:
                print(todos, "todos")
                return todos
        # return {"message": "Not able to find"}
        raise HTTPException(404, detail={"error" : "Not able to find"})

def posttogetPrameter(req:reqBody):
    print(req,"request",req.model_dump())
    data.append({
        "id":len(data) + 1,
        **req.model_dump()
    })
    return {"message": "Task Created"}


def posttogetPrameterdelete(id:int):
    # print(req,"request",req.model_dump())
    # data.pop(id)
    # return {"message": "Task Deleted"}
    for index, todo in enumerate(data):
        if todo["id"] == id:
            data.pop(index)
            return {"message": "Task Deleted"}

    raise HTTPException(
        status_code=404,
        detail={"error": "Task not found"}
    )
