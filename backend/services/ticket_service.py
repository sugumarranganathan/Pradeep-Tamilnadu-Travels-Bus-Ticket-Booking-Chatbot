"""
Ticket Service
"""

from datetime import datetime
import uuid


class TicketService:

    def generate_ticket(self, booking):

        ticket = {

            "ticket_number":
            f"PT-{uuid.uuid4().hex[:8].upper()}",

            "booking_date":
            datetime.now().strftime("%d-%m-%Y"),

            "journey_date":
            booking.get("journey_date", "Not Selected"),

            "passenger_name":
            booking["name"],

            "mobile":
            booking["mobile"],

            "age":
            booking["age"],

            "gender":
            booking["gender"],

            "route":
            booking["route"],

            "bus_number":
            booking["bus"],

            "departure_time":
            booking["time"],

            "seat":
            booking["seat"],

            "status":
            "Confirmed"

        }

        return ticket
