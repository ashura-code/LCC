# Comment

## Overview
The comment management domain is responsible for creating and managing comments related to tickets.

## API Endpoints
- **POST** `/comments` — Create a new comment

## Entities
- **Comment**: id, message, ticket
- **Ticket**: id

## Business Logic
- Create a new comment and associate it with a ticket

## Usage Examples
- Create a new comment: POST /comments with a JSON body containing the comment message and ticket id
- Example JSON body: {"message": "This is a comment", "ticket": {"id": 1}}
