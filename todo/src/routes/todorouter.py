from fastapi import APIRouter
from src.contollers.todocontroller import todoget,posttogetPrameter,posttogetParams,posttogetPrameterdelete
from src.dtos import reqBody


todoRouter = APIRouter(prefix="/todo")

@todoRouter.get("/")
def getTodo():
    return todoget()

@todoRouter.get("/{todoId}", status_code=200)
def postTodo(todoId:int):
    print(todoId,"routeId")
    return posttogetParams(todoId)

# //topost something in body we go with pydantic approach
@todoRouter.post("/")
def postTodo(req:reqBody):
    # print(routeId,"routeId")
    return posttogetPrameter(req)

@todoRouter.delete("/{id}")
def postTodo(id:int):
    # print(routeId,"routeId")
    return posttogetPrameterdelete(id)

