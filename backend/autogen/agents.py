"""
AutoGen Agent Definitions
"""


class RouteAgent:

    def execute(self, query):

        return {
            "agent": "Route Agent",
            "message": "Route information processed."
        }


class BookingAgent:

    def execute(self, query):

        return {
            "agent": "Booking Agent",
            "message": "Booking request processed."
        }


class TicketAgent:

    def execute(self, query):

        return {
            "agent": "Ticket Agent",
            "message": "Ticket generated."
        }


class SupportAgent:

    def execute(self, query):

        return {
            "agent": "Support Agent",
            "message": "Support request processed."
        }
