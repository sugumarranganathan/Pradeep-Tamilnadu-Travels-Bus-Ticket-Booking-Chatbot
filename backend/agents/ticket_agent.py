"""
Ticket Agent
"""

from services.ticket_service import TicketService

from ticket.image_generator import TicketImageGenerator
from ticket.pdf_generator import PDFGenerator


class TicketAgent:

    def __init__(self):

        self.ticket_service = TicketService()

        self.image_generator = TicketImageGenerator()

        self.pdf_generator = PDFGenerator()

    def generate(self, booking):

        ticket = self.ticket_service.generate_ticket(
            booking
        )

        image = self.image_generator.generate(
            ticket
        )

        pdf = self.pdf_generator.generate(
            ticket
        )

        return {

            "ticket": ticket,

            "image": image,

            "pdf": pdf

        }
