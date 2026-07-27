"""
Conversation State Machine
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
Version 1.0
"""

from enum import Enum


class ConversationState(str, Enum):

    WELCOME = "WELCOME"

    MAIN_MENU = "MAIN_MENU"

    ROUTE_SELECTION = "ROUTE_SELECTION"

    BUS_SELECTION = "BUS_SELECTION"

    TIME_SELECTION = "TIME_SELECTION"

    SEAT_SELECTION = "SEAT_SELECTION"

    PASSENGER_NAME = "PASSENGER_NAME"

    MOBILE_NUMBER = "MOBILE_NUMBER"

    AGE = "AGE"

    GENDER = "GENDER"

    CONFIRM_BOOKING = "CONFIRM_BOOKING"

    GENERATE_TICKET = "GENERATE_TICKET"

    COMPLETED = "COMPLETED"
