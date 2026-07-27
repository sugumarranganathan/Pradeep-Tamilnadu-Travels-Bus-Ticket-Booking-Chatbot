"""
Agent Team
"""

from backend.agents.booking_agent import BookingAgent
from backend.agents.ticket_agent import TicketAgent
from backend.agents.support_agent import SupportAgent
from backend.agents.supervisor_agent import SupervisorAgent


class AgentTeam:

    def __init__(self):
        self.booking = BookingAgent()
        self.ticket = TicketAgent()
        self.support = SupportAgent()
        self.supervisor = SupervisorAgent()
