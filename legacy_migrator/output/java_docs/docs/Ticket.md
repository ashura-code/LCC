# Ticket

## Overview
A system for managing tickets with different statuses

## API Endpoints
- **GET** `/tickets` — Get all tickets
- **POST** `/tickets` — Create a new ticket
- **PUT** `/tickets/{id}/status` — Update the status of a ticket

## Entities
- **Ticket**: id, title, description, status
- **Comment**: id, text, ticketId

## Enums
- OPEN
- IN_PROGRESS
- CLOSED

## Business Logic
- A ticket can be created with a title, description, and initial status
- A ticket's status can be updated
- All tickets can be retrieved

## Usage Examples
- Create a new ticket: POST /tickets with a JSON body containing title and description
- Get all tickets: GET /tickets
- Update a ticket's status: PUT /tickets/{id}/status with a query parameter status
