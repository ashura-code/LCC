# Python FastAPI System Documentation

## Introduction
The system provides a range of features, including the ability to create new tickets, retrieve all tickets, and update the status of existing tickets. The system also provides the ability to create new comments associated with tickets. The system is designed to be highly flexible and can be easily extended to meet the needs of a variety of use cases.

## Architecture
The system architecture consists of a single API endpoint, which provides access to the Ticket and Comment domains. The API endpoint is built using the FastAPI framework and provides a RESTful interface for interacting with the system. The system utilizes a database to store ticket and comment data, and provides a range of services for creating, retrieving, and updating this data.

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
- POST /tickets with JSON body: {"title": "New Ticket", "description": "This is a new ticket", "status": "OPEN"}
- GET /tickets
- POST /comments with JSON body: {"message": "This is a new comment", "ticket": 1}

## Domains
- [Ticket](Ticket.md)
- [Comment](Comment.md)
