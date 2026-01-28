# Python FastAPI System Documentation

## Introduction
The ticket management system is designed to handle the creation, retrieval, and updating of tickets with different statuses. The system consists of two main domains: Ticket and Comment. The Ticket domain handles the management of tickets, including creating new tickets, retrieving all tickets, and updating the status of existing tickets. The Comment domain handles the creation of comments for tickets. The system uses a RESTful API architecture, with endpoints for creating, reading, and updating resources.

## Architecture
The system uses a microservices architecture, with two main services: Ticket Service and Comment Service. The Ticket Service handles all operations related to tickets, including creating, retrieving, and updating tickets. The Comment Service handles the creation of comments for tickets. The services communicate with each other using RESTful APIs. The system uses FastAPI as the web framework, Pydantic for data validation, and Uvicorn as the ASGI server.

## Requirements
- Python 3.10+
- fastapi
- uvicorn
- pydantic

## Installation
- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

## How To Run
- uvicorn main:app --reload
- Open http://127.0.0.1:8000/docs

## Usage Examples
- {
  "method": "POST",
  "path": "/tickets",
  "description": "Create a new ticket",
  "request_body": {
    "title": "Example Ticket",
    "description": "This is an example ticket",
    "status": "OPEN"
  },
  "response": {
    "id": 1,
    "title": "Example Ticket",
    "description": "This is an example ticket",
    "status": "OPEN"
  }
}
- {
  "method": "GET",
  "path": "/tickets",
  "description": "Get all tickets",
  "response": [
    {
      "id": 1,
      "title": "Example Ticket",
      "description": "This is an example ticket",
      "status": "OPEN"
    },
    {
      "id": 2,
      "title": "Another Ticket",
      "description": "This is another ticket",
      "status": "IN_PROGRESS"
    }
  ]
}
- {
  "method": "POST",
  "path": "/comments",
  "description": "Create a new comment",
  "request_body": {
    "message": "This is a comment",
    "ticket": 1
  },
  "response": {
    "id": 1,
    "message": "This is a comment",
    "ticket": 1
  }
}
- {
  "method": "PUT",
  "path": "/tickets/1/status",
  "description": "Update the status of a ticket",
  "request_body": {
    "status": "IN_PROGRESS"
  },
  "response": {
    "id": 1,
    "title": "Example Ticket",
    "description": "This is an example ticket",
    "status": "IN_PROGRESS"
  }
}

## Domains
- [Ticket](Ticket.md)
- [Comment](Comment.md)
