from fastapi import FastAPI
from api.router import api_router

app = FastAPI(
    title="Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot",
    description="AI-Powered Multi-Agent Bus Ticket Booking Chatbot using Groq, AutoGen & RAG",
    version="1.0.0"
)

app.include_router(api_router)
