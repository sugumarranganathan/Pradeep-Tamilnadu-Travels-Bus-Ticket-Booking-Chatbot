"""
AutoGen Workflow
"""


from backend.autogen.team import AgentTeam


class AgentWorkflow:

    def __init__(self):

        self.team = AgentTeam()

    def process(self, task):

        task = task.lower()

        if any(word in task for word in ["route", "madurai", "coimbatore", "salem", "trichy"]):
            return self.team.route.execute(task)

        elif any(word in task for word in ["book", "booking", "ticket"]):
            return self.team.booking.execute(task)

        elif any(word in task for word in ["generate", "pdf"]):
            return self.team.ticket.execute(task)

        else:
            return self.team.support.execute(task)
