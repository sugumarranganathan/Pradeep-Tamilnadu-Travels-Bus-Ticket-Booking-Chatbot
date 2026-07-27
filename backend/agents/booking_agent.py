"""
Booking Agent
"""


from backend.services.booking_service import get_routes


class BookingAgent:

    def start_booking(self):

        return {

            "step": "route_selection",

            "message": "Select Your Route",

            "routes": get_routes()

        }
