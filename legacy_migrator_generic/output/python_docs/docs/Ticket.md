# Ticket

## Overview
A system for managing tickets with their respective status

## API Routes
- **GET** `/tickets` → `Retrieve all tickets`
- **POST** `/tickets` → `Create a new ticket`
- **PUT** `/tickets/{id}/status` → `Update the status of a ticket`

## Models
- **Ticket**: id, title, description, status
- **Comment**: id, text, ticketId

## Enums
- OPEN
- IN_PROGRESS
- CLOSED

## Services
- A ticket can be created with a title, description, and initial status
- A ticket's status can be updated
- All tickets can be retrieved
