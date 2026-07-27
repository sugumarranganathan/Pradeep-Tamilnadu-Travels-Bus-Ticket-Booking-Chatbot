"""
Agent Team
"""

from autogen.agents import (
    RouteAgent,
    BookingAgent,
    TicketAgent,
    SupportAgent
)


class AgentTeam:

    def __init__(self):

        self.route = RouteAgent()
        self.booking = BookingAgent()
        self.ticket = TicketAgent()
        self.support = SupportAgent()
