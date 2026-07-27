from fastapi import APIRouter

router = APIRouter()

@router.get("/booking/menu")
def booking_menu():

    return {
        "title": "Bus Ticket Booking",
        "options": [
            "1. Chennai → Madurai",
            "2. Chennai → Coimbatore",
            "3. Chennai → Trichy",
            "4. Chennai → Salem"
        ]
    }
