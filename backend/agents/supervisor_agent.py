"""
Supervisor Agent

Routes the customer's request to the appropriate agent.
"""

from backend.agents.booking_agent import BookingAgent
from backend.agents.support_agent import SupportAgent


class SupervisorAgent:

    def __init__(self):
        self.booking_agent = BookingAgent()
        self.support_agent = SupportAgent()

    def process(self, option):

        if option == "1":
            return self.booking_agent.start_booking()

        elif option == "6":
            return self.support_agent.reply()

        return {
            "message": "Please choose a valid option."
        }
