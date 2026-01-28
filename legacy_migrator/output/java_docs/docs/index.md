# Legacy Java System Documentation

## Introduction
This system provides a backend for managing tickets and their respective comments. It allows users to create, update, and retrieve tickets, as well as create comments for existing tickets.

## Architecture
The system consists of two main domains: Ticket and Comment. The Ticket domain handles ticket creation, retrieval, and status updates, while the Comment domain handles comment creation. The system uses a RESTful API to expose endpoints for these operations.

## Requirements
- Java Runtime Environment (JRE) installed
- A compatible IDE or text editor for development
- A database management system for storing ticket and comment data

## Installation
- Clone the repository to your local machine
- Install required dependencies using your preferred package manager
- Configure the database connection settings to match your environment

## How To Run
- Compile the Java code using the command 'javac'
- Run the application using the command 'java'
- Use a tool like Postman or cURL to test API endpoints

## Usage Examples
- Create a new ticket: POST /tickets with a JSON body containing title and description
- Update a ticket's status: PUT /tickets/{id}/status with a query parameter status
- Retrieve all tickets: GET /tickets
- Create a new comment: POST /comments with JSON body {"message": "Example comment", "ticket": {"id": 1}}

## Domains
- [Ticket](Ticket.md)
- [Comment](Comment.md)
