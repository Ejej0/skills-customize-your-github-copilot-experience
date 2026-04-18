# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework to practice route creation, request handling, and JSON responses in Python.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Use the starter code to build a small API for managing books. Define routes that allow users to fetch all books and add a new book.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Add a `GET /books` endpoint that returns a list of books as JSON
- Add a `POST /books` endpoint that accepts a new book and stores it in memory

### 🛠️ Implement Lookup and Validation

#### Description
Expand the API with an endpoint to fetch a single book by ID and return helpful errors when the requested item does not exist.

#### Requirements
Completed program should:

- Add a `GET /books/{book_id}` endpoint
- Return the matching book when the ID exists
- Return an appropriate error response when a book is not found
- Keep responses clear and consistent for API users
