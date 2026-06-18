from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books_store = []

class Books(BaseModel):
    book_id: int
    title: str
    author: str
    available: bool

@app.post("/book")
def add_book(book: Books):
    books_store.append(book)

    return {
        "message" : "Book successfully added"
    }

@app.get("/book")
def get_all_books():

    return books_store

@app.get("/book/{book_id}")
def get_one_book(book_id: int):

    for book in books_store:

        if book.book_id == book_id:

            return book
        
    return{
        "message" : "No book found"
        }
    
@app.put("/book/{book_id}")
def update_book(book_id: int, updated_book: Books):

    for index, book in enumerate(books_store):

        if book.book_id == book_id:

            books_store[index] = updated_book

            return {
                "message" : "book updated successfully",
                "book" : updated_book
            }
    return {
        "message" : "book not found"
    }

@app.delete("/book/{book_id}")
def delete_book(book_id: int):

    for index, book in enumerate(books_store):

        if book.book_id == book_id:
            
            books_store.pop(index)

            return{
                "message" : "book successfully removed"
            }
    return{
        "message" : "unable to remove book"
    }
