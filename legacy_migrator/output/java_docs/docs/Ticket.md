# Ticket

## Overview
A system for managing and tracking tickets, including creating, updating, and retrieving ticket information.

## API Endpoints
- **GET** `/tickets` — Retrieve a list of all tickets.
- **POST** `/tickets` — Create a new ticket.
- **PUT** `/tickets/{id}/status` — Update the status of a ticket with the given ID.

## Entities
- **Ticket**: id, title, description, status
- **TicketStatus**: OPEN, IN_PROGRESS, CLOSED

## Enums
- TicketStatus

## Business Logic
- Tickets can be created with a title, description, and initial status.
- Tickets can be updated to change their status.
- Tickets can be retrieved by ID or in a list of all tickets.

## Usage Examples
- Create a new ticket: POST /tickets with a JSON body containing title and description.
- Update the status of a ticket: PUT /tickets/{id}/status with a query parameter status.
- Retrieve a list of all tickets: GET /tickets
