"""
Booking Flow
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

from backend.conversation.state_machine import ConversationState
from conversation.menu import (
    ROUTE_MENU,
    BUS_MENU,
    TIME_MENU,
    GENDER_MENU,
    CONFIRM_MENU,
)

from conversation.seat_layout import SeatLayout
from services.data_service import DataService


class BookingFlow:

    def __init__(self):

        self.seat_layout = SeatLayout()
        self.data_service = DataService()

    def process(self, session, user_input):

        state = session.get_state()

        # -------------------------------
        # Route Selection
        # -------------------------------
        if state == ConversationState.ROUTE_SELECTION:

            routes = self.data_service.get_routes()

            route_map = {}

            for route in routes:

                route_map[str(route["id"])] = (
                    f'{route["from"]} → {route["to"]}'
                )

            if user_input not in route_map:
                return ROUTE_MENU

            session.update(
                "route",
                route_map[user_input]
            )

            session.set_state(
                ConversationState.BUS_SELECTION
            )

            return BUS_MENU

        # -------------------------------
        # Bus Selection
        # -------------------------------
        elif state == ConversationState.BUS_SELECTION:

            buses = self.data_service.get_buses()

            bus_map = {}

            for bus in buses:

                bus_map[str(bus["id"])] = bus["bus_no"]

            if user_input not in bus_map:
                return BUS_MENU

            session.update(
                "bus",
                bus_map[user_input]
            )

            session.set_state(
                ConversationState.TIME_SELECTION
            )

            return TIME_MENU

        # -------------------------------
        # Time Selection
        # -------------------------------
        elif state == ConversationState.TIME_SELECTION:

            timings = self.data_service.get_timings()

            time_map = {}

            for timing in timings:

                time_map[str(timing["id"])] = timing["time"]

            if user_input not in time_map:
                return TIME_MENU

            session.update(
                "time",
                time_map[user_input]
            )

            session.set_state(
                ConversationState.SEAT_SELECTION
            )

            return self.seat_layout.get_layout()

        # -------------------------------
        # Seat Selection
        # -------------------------------
        elif state == ConversationState.SEAT_SELECTION:

            seat = user_input.upper()

            if self.seat_layout.is_available(seat):

                self.seat_layout.book(seat)

                session.update(
                    "seat",
                    seat
                )

                session.set_state(
                    ConversationState.PASSENGER_NAME
                )

                return "👤 Enter Passenger Name"

            return (
                "❌ Seat not available.\n\n"
                + self.seat_layout.get_layout()
            )

        # -------------------------------
        # Passenger Name
        # -------------------------------
        elif state == ConversationState.PASSENGER_NAME:

            session.update(
                "name",
                user_input
            )

            session.set_state(
                ConversationState.MOBILE_NUMBER
            )

            return "📱 Enter Mobile Number"

        # -------------------------------
        # Mobile Number
        # -------------------------------
        elif state == ConversationState.MOBILE_NUMBER:

            session.update(
                "mobile",
                user_input
            )

            session.set_state(
                ConversationState.AGE
            )

            return "🎂 Enter Passenger Age"

        # -------------------------------
        # Passenger Age
        # -------------------------------
        elif state == ConversationState.AGE:

            session.update(
                "age",
                user_input
            )

            session.set_state(
                ConversationState.GENDER
            )

            return GENDER_MENU

        # -------------------------------
        # Gender
        # -------------------------------
        elif state == ConversationState.GENDER:

            genders = {
                "1": "Male",
                "2": "Female"
            }

            if user_input not in genders:
                return GENDER_MENU

            session.update(
                "gender",
                genders[user_input]
            )

            session.set_state(
                ConversationState.CONFIRM_BOOKING
            )

            return CONFIRM_MENU

        # -------------------------------
        # Confirm Booking
        # -------------------------------
        elif state == ConversationState.CONFIRM_BOOKING:

            if user_input == "1":

                session.set_state(
                    ConversationState.GENERATE_TICKET
                )

                return "🎫 Generating your ticket..."

            elif user_input == "2":

                session.set_state(
                    ConversationState.MAIN_MENU
                )

                return "❌ Booking Cancelled."

            return CONFIRM_MENU

        return ROUTE_MENU
