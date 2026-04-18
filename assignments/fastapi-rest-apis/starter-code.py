from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}


# TODO: Task 1 - Return all books
@app.get("/books")
def get_books():
    return books


# TODO: Task 1 - Add a new book
@app.post("/books")
def create_book(book: Book):
    books.append(book.model_dump())
    return {"message": "Book added", "book": book}


# TODO: Task 2 - Get one book by id and handle not found cases
@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
