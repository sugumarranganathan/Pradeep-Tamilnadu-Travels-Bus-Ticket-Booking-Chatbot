"""
Session Manager
"""

from backend.conversation.state_machine import ConversationState

class SessionManager:

    def __init__(self):

        self.state = ConversationState.WELCOME

        self.booking = {
            "route": "",
            "bus": "",
            "time": "",
            "seat": "",
            "name": "",
            "mobile": "",
            "age": "",
            "gender": ""
        }

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def update(self, key, value):
        self.booking[key] = value

    def get_booking(self):
        return self.booking
