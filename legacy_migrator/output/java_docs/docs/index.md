# Legacy Java System Documentation

## Introduction
This system provides a backend for managing tickets and comments. It allows users to create, update, and retrieve tickets, as well as create comments associated with tickets.

## Architecture
The system consists of two main domains: Ticket and Comment. The Ticket domain handles ticket creation, retrieval, and status updates, while the Comment domain handles comment creation. The system uses a RESTful API with JSON data format.

## Requirements
- Java runtime environment
- HTTP client or API testing tool
- JSON parsing library (if necessary)

## Installation
- Clone the repository containing the system code
- Build the project using the provided build script
- Start the server using the provided run script

## How To Run
- Use a HTTP client or API testing tool to send requests to the server
- Send a GET request to /tickets to retrieve all tickets
- Send a POST request to /tickets with a JSON body containing title and description to create a new ticket
- Send a PUT request to /tickets/{id}/status with a query parameter status to update a ticket's status
- Send a POST request to /comments with a JSON body containing message and ticket to create a new comment

## Usage Examples
- Create a new ticket: POST /tickets with a JSON body containing title and description
- Get all tickets: GET /tickets
- Update a ticket's status: PUT /tickets/{id}/status with a query parameter status
- Create a new comment: POST /comments with a JSON body containing message and ticket

## Domains
- [Ticket](Ticket.md)
- [Comment](Comment.md)
