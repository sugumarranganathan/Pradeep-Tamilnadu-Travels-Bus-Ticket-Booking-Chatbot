"""
Ticket Agent
"""

from services.ticket_service import TicketService


class TicketAgent:

    def __init__(self):

        self.ticket_service = TicketService()

    def generate(self, booking):

        return self.ticket_service.generate_ticket(
            booking
        )
