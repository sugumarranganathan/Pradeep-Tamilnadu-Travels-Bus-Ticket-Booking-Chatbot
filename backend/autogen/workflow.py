"""
Agent Workflow
"""

from autogen.team import AgentTeam


class AgentWorkflow:

    def __init__(self):

        self.team = AgentTeam()

    def process(self, task):

        task = task.lower()

        if "route" in task:

            return self.team.route.execute(task)

        if "book" in task:

            return self.team.booking.execute(task)

        if "ticket" in task:

            return self.team.ticket.execute(task)

        return self.team.support.execute(task)
