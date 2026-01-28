# Comment

## Overview
Handles creation of comments for tickets

## API Endpoints
- **POST** `/comments` — Creates a new comment

## Entities
- **Comment**: id, message, ticket

## Business Logic
- Create a new comment and associate it with a ticket

## Usage Examples
- Create a new comment: POST /comments with JSON body {"message": "Example comment", "ticket": {"id": 1}}
