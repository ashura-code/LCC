from fastapi import FastAPI

from routers import ticket
from routers import comment

app = FastAPI()

app.include_router(ticket.router)
app.include_router(comment.router)
