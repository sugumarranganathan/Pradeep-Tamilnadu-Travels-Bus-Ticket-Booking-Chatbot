from fastapi import APIRouter

router = APIRouter()

@router.get("/ticket/sample")
def sample_ticket():

    return {
        "ticket_number": "PT202600001",
        "passenger_name": "Sugumar",
        "route": "Chennai → Coimbatore",
        "bus_number": "PT101",
        "seat_number": "B3",
        "departure_time": "09:30 AM",
        "journey_date": "15-Aug-2026",
        "fare": "₹950",
        "status": "Confirmed"
    }
