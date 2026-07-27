from fastapi import APIRouter

from backend.api.health import router as health_router
from backend.api.chatbot import router as chatbot_router
from backend.api.booking import router as booking_router
from backend.api.ticket import router as ticket_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router, tags=["Health"])
api_router.include_router(chatbot_router, tags=["Chatbot"])
api_router.include_router(booking_router, tags=["Booking"])
api_router.include_router(ticket_router, tags=["Ticket"])
