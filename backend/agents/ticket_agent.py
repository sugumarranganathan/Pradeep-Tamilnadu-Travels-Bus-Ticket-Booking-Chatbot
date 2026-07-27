"""
Ticket Agent
"""

from services.ticket_service import create_ticket


class TicketAgent:

    def generate(self, booking_data):

        return create_ticket(booking_data)
