"""
Chatbot Service
"""

WELCOME_MESSAGE = """
🚌 Welcome to Pradeep Tamilnadu Travels

Please choose an option.

1. Book Ticket
2. Bus Timings
3. Fare Details
4. Available Routes
5. Cancellation
6. Customer Support
"""


def get_welcome_message():
    return WELCOME_MESSAGE


def process_menu(option: str):

    menu = {

        "1": "BOOK_TICKET",

        "2": "BUS_TIMINGS",

        "3": "FARE_DETAILS",

        "4": "AVAILABLE_ROUTES",

        "5": "CANCELLATION",

        "6": "CUSTOMER_SUPPORT"

    }

    return menu.get(option, "INVALID")
