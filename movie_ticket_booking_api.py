from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TicketBooking(BaseModel):
    booking_id: int
    customer_name: str
    movie_name: str
    tickets: int

bookings = []

@app.post("/bookings")
def add_booking(ticket: TicketBooking):

    if ticket.tickets > 10:

        return {
            "message" : "maximum 10 tickets allowed"
        }

    bookings.append(ticket)

    return {
        "message" : "Booking created successfully"
    }

@app.get("/bookings")
def get_bookings():

    return bookings

@app.get("/bookings/search")
def search_booking(movie_name: str):

    matched_bookings = []

    for booking in bookings:

        if booking.movie_name == movie_name:

            matched_bookings.append(booking)

    return matched_bookings

@app.get("/bookings/{booking_id}")
def get_one_booking(booking_id: int):

    for booking in bookings:

        if booking.booking_id == booking_id:

            return booking
    return {
        "message" : "Booking not found"
    }

@app.put("/bookings/{booking_id}")
def update_booking(booking_id: int, new_booking: TicketBooking):

    for index, booking in enumerate(bookings):

        if booking.booking_id == booking_id:

            bookings[index] = new_booking

            return{
                "message" : "booking updated successfully"
            }
    return {
        "message" : "unable to update booking"
    }

@app.delete("/bookings/{booking_id}")
def cancel_booking(booking_id: int):

    for index, booking in enumerate(bookings):

        if booking.booking_id == booking_id:

            bookings.pop(index)

            return{
                "message" : "booking canceled successfully",
                "deleted booking" : booking
            }
        
    return {
        "message" : "unable to cancel booking"
    }
