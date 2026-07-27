"""
AutoGen Workflow
"""


class AgentWorkflow:

    def __init__(self):
        pass

    def process(self, task):
        """
        Placeholder workflow.

        ConversationManager already controls the booking flow,
        ticket generation, and support responses.
        """
        print(f"[AgentWorkflow] Task received: {task}")

        return {
            "status": "success",
            "task": task
        }
