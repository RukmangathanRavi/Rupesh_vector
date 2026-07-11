from pydantic import BaseModel

class reqBody(BaseModel):
    name:str
    sex:str