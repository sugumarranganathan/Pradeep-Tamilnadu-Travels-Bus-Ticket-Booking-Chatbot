from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    return {
        "user_message": request.message,
        "bot_message": "Welcome to Pradeep Tamilnadu Travels. Please select an option:\n\n1. Book Ticket\n2. Bus Timings\n3. Fare Details\n4. Available Routes\n5. Cancellation\n6. Customer Support"
    }
