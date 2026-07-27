"""
AutoGen Workflow
"""

from backend.autogen.team import AgentTeam


class AgentWorkflow:

    def __init__(self):
        self.team = AgentTeam()

    def process(self, task):

        task = task.lower()

        # -----------------------------
        # Booking / Route
        # -----------------------------
        if any(word in task for word in [
            "book", "booking", "ticket",
            "route", "madurai",
            "coimbatore", "salem",
            "trichy", "chennai",
            "bus", "travel"
        ]):
            return self.team.booking.start_booking()

        # -----------------------------
        # Generate Ticket
        # -----------------------------
        elif any(word in task for word in [
            "generate", "pdf"
        ]):

            # Ticket generation is handled by ConversationManager
            return {
                "status": "Ticket generation started"
            }

        # -----------------------------
        # Support
        # -----------------------------
        else:
            return {
                "status": "Support request received"
            }
