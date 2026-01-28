# Legacy Java System Documentation

<<<<<<< Updated upstream
## System Overview
Legacy Spring Boot Ticket Tracking system handling tickets and comments.
=======
## Introduction
The backend system is designed to manage and track tickets, including creating, updating, and retrieving ticket information, as well as creating and managing comments related to tickets.

## Architecture
The system consists of two main domains: Ticket and Comment. The Ticket domain handles ticket creation, update, and retrieval, while the Comment domain handles comment creation and management. The system uses RESTful API endpoints to interact with the domains.

## Requirements
- Java Runtime Environment (JRE) installed
- API endpoint URLs and authentication credentials
- JSON body format for API requests

## Installation
- Clone the repository from the version control system
- Build the project using the build tool (e.g. Maven or Gradle)
- Deploy the application to a server or cloud platform

## How To Run
- Start the application server
- Use a tool like Postman or cURL to send HTTP requests to the API endpoints
- Authenticate with the API using the provided credentials

## Usage Examples
- Create a new ticket: POST /tickets with a JSON body containing title and description
- Update the status of a ticket: PUT /tickets/{id}/status with a query parameter status
- Retrieve all tickets: GET /tickets
- Create a new comment: POST /comments with a JSON body containing the comment message and ticket id
- Example JSON body for comment creation: {"message": "This is a comment", "ticket": {"id": 1}}
>>>>>>> Stashed changes

## Domains
- [Ticket](Ticket.md)
- [Comment](Comment.md)
