"""
AutoGen Workflow
"""

from backend.autogen.team import AgentTeam


class AgentWorkflow:

    def __init__(self):
        self.team = AgentTeam()

    def process(self, task):

        task = task.lower().strip()

        # Book Ticket
        if "book" in task or "booking" in task:
            return self.team.supervisor.process("1")

        # Customer Support
        elif "support" in task:
            return self.team.supervisor.process("6")

        # Route / Timings / Fare
        elif any(word in task for word in [
            "route",
            "timing",
            "fare",
            "madurai",
            "coimbatore",
            "salem",
            "trichy",
            "chennai",
            "bus"
        ]):
            return {
                "message": "Route information requested."
            }

        # Ticket Generation
        elif "generate" in task or "pdf" in task:
            return {
                "message": "Ticket generation handled by ConversationManager."
            }

        # Default
        return {
            "message": "Task received."
        }
