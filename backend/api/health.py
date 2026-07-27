from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "success",
        "message": "Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot API is running",
        "version": "1.0.0"
    }
