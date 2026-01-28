from pydantic import BaseModel

class Ticket(BaseModel):
    id: str
    title: str
    description: str
    status: str

class Comment(BaseModel):
    id: str
    text: str
    ticketId: str
