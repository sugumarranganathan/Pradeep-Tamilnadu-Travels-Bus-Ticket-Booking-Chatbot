"""
Booking Flow
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

from conversation.state_machine import ConversationState
from conversation.menu import (
    ROUTE_MENU,
    BUS_MENU,
    TIME_MENU,
    GENDER_MENU,
    CONFIRM_MENU,
)


class BookingFlow:

    def process(self, session, user_input):

        state = session.get_state()

        # -------------------------------
        # Route Selection
        # -------------------------------
        if state == ConversationState.ROUTE_SELECTION:

            routes = {
                "1": "Chennai → Madurai",
                "2": "Chennai → Coimbatore",
                "3": "Chennai → Salem",
                "4": "Chennai → Trichy",
            }

            session.update("route", routes.get(user_input, ""))

            session.set_state(ConversationState.BUS_SELECTION)

            return BUS_MENU

        # -------------------------------
        # Bus Selection
        # -------------------------------
        elif state == ConversationState.BUS_SELECTION:

            buses = {
                "1": "PT101",
                "2": "PT102",
                "3": "PT103",
            }

            session.update("bus", buses.get(user_input, ""))

            session.set_state(ConversationState.TIME_SELECTION)

            return TIME_MENU

        # -------------------------------
        # Time Selection
        # -------------------------------
        elif state == ConversationState.TIME_SELECTION:

            times = {
                "1": "08:00 AM",
                "2": "09:30 AM",
                "3": "10:30 PM",
            }

            session.update("time", times.get(user_input, ""))

            session.set_state(ConversationState.SEAT_SELECTION)

            return "Enter Seat Number (Example: B3)"

        # -------------------------------
        # Seat
        # -------------------------------
        elif state == ConversationState.SEAT_SELECTION:

            session.update("seat", user_input)

            session.set_state(ConversationState.PASSENGER_NAME)

            return "Passenger Name"

        # -------------------------------
        # Passenger Name
        # -------------------------------
        elif state == ConversationState.PASSENGER_NAME:

            session.update("name", user_input)

            session.set_state(ConversationState.MOBILE_NUMBER)

            return "Mobile Number"

        # -------------------------------
        # Mobile
        # -------------------------------
        elif state == ConversationState.MOBILE_NUMBER:

            session.update("mobile", user_input)

            session.set_state(ConversationState.AGE)

            return "Passenger Age"

        # -------------------------------
        # Age
        # -------------------------------
        elif state == ConversationState.AGE:

            session.update("age", user_input)

            session.set_state(ConversationState.GENDER)

            return GENDER_MENU

        # -------------------------------
        # Gender
        # -------------------------------
        elif state == ConversationState.GENDER:

            gender = {
                "1": "Male",
                "2": "Female",
            }

            session.update("gender", gender.get(user_input, ""))

            session.set_state(ConversationState.CONFIRM_BOOKING)

            return CONFIRM_MENU

        # -------------------------------
        # Confirm
        # -------------------------------
        elif state == ConversationState.CONFIRM_BOOKING:

            if user_input == "1":

                session.set_state(
                    ConversationState.GENERATE_TICKET
                )

                return "Generating your ticket..."

            session.set_state(ConversationState.MAIN_MENU)

            return "Booking Cancelled."

        return ROUTE_MENU
