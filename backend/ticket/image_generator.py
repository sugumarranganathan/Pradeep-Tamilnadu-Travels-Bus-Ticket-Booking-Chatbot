"""
Ticket Image Generator
Version 1
"""

from backend.ticket.ticket_template import TicketTemplate


class TicketImageGenerator:

    def generate(self, ticket):

        ticket_text = TicketTemplate.get_ticket(ticket)

        return {

            "image_name": f'{ticket["ticket_number"]}.png',

            "content": ticket_text

        }
