from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Reservations(BaseModel):
    booking_id: int
    customer_name: str
    room_type: str
    nights: int


room_types = ["standard", "deluxe", "suite"]
guests = []

room_prices = {
    "standard" : 100,
    "deluxe" : 200,
    "suite" : 500
}

@app.post("/reservations")
def add_reservation(guest: Reservations):
        
        guest.room_type = guest.room_type.lower()

        if guest.room_type.lower() not in room_types:

            return{
                "message" : "please select valid room type"
                }
            
        guests.append(guest)

        return {
            "message" : "Reservation created successfully"
        }

@app.get("/reservations/search")
def search_booking(room_type: str):

    room_list = []

    for booking in guests:

        if booking.room_type.lower() == room_type.lower():

            room_list.append(booking)

    return room_list

@app.get("/reservations/{booking_id}")
def get_one_guest(booking_id: int):

    for guest in guests:

        if guest.booking_id == booking_id:

            return guest
    
    return{
        "message" : "unable to find guest"
    }


@app.get("/reservations")
def get_reservations():

    return guests


@app.delete("/reservations/{booking_id}")
def delete_reservation(booking_id: int):

    for index, guest in enumerate (guests):

        if guest.booking_id == booking_id:

            guests.pop(index)

            return{
                "message" : "reservation successfully canceled"
            }

    return {
        "message" : "invalid booking id mentioned"
    }

@app.put("/reservations/{booking_id}")
def update_booking(booking_id: int, new_booking: Reservations):

    new_booking.room_type = new_booking.room_type.lower()

    if new_booking.room_type not in room_types:
        return {
            "message": "please select valid room type"
        }

    for index, booking in enumerate(guests):

        if booking.booking_id == booking_id:

            guests[index] = new_booking

            return{
                "message" : "booking updated successfully created"
            }
    return{
        "message" : "invalid booking id entered"
    }

@app.get("/reservations/{booking_id}/bill")
def get_bill(booking_id: int):

    for booking in guests:

        if booking.booking_id == booking_id:

            price = room_prices[booking.room_type]
            total_bill = price * booking.nights
            
            return{
                "booking_id" : booking_id,
                "customer_name" : booking.customer_name,
                "total_bill" : total_bill
            }
    
    return {
        "message" : "booking not found"
    }
