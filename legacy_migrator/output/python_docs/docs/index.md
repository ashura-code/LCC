# Python FastAPI System Documentation

## Introduction
This is a FastAPI backend for managing tickets and comments. It provides endpoints for creating, updating, and retrieving ticket information, as well as creating comments related to tickets.

## Architecture
The backend is divided into two domains: Ticket and Comment. The Ticket domain handles ticket-related operations, while the Comment domain handles comment-related operations. Both domains use services (TicketService and CommentService) to encapsulate business logic.

## Requirements
- Python 3.8 or higher
- FastAPI 0.92.0 or higher
- Uvicorn 0.18.3 or higher
- Pydantic 1.10.2 or higher

## Installation
- Clone the repository using git clone
- Install dependencies using pip install -r requirements.txt
- Create a new virtual environment using python -m venv venv
- Activate the virtual environment using source venv/bin/activate (on Linux/Mac) or venv\Scripts\activate (on Windows)

## How To Run
- Run the application using uvicorn main:app --host 0.0.0.0 --port 8000
- Access the API documentation at http://localhost:8000/docs
- Use a tool like curl or Postman to test the API endpoints

## Usage Examples
- Create a new ticket: POST /tickets with JSON body {"title": "New Ticket", "description": "This is a new ticket"}
- Get all tickets: GET /tickets
- Update a ticket's status: PUT /tickets/{id}/status with JSON body {"status": "IN_PROGRESS"}
- Create a new comment: POST /comments with JSON body {"message": "This is a new comment", "ticket_id": 1}

## Domains
- [Ticket](Ticket.md)
- [Comment](Comment.md)
