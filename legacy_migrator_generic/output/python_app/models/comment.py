from pydantic import BaseModel

class Comment(BaseModel):
    id: str
    message: str
    ticket: str
