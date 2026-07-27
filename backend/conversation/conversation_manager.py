"""
Conversation Manager
"""

from conversation.menu import WELCOME_MENU
from conversation.state_machine import ConversationState
from conversation.booking_flow import BookingFlow
from conversation.session_manager import SessionManager


class ConversationManager:

    def __init__(self):

        self.session = SessionManager()

        self.flow = BookingFlow()

    def reply(self, user_message):

        state = self.session.get_state()

        # Welcome
        if state == ConversationState.WELCOME:

            self.session.set_state(
                ConversationState.MAIN_MENU
            )

            return WELCOME_MENU

        # Main Menu
        if state == ConversationState.MAIN_MENU:

            if user_message == "1":

                self.session.set_state(
                    ConversationState.ROUTE_SELECTION
                )

                return """
Select Route

1. Chennai → Madurai

2. Chennai → Coimbatore

3. Chennai → Salem

4. Chennai → Trichy
"""

            return "Please choose option 1 to continue."

        # Booking Flow
        return self.flow.process(
            self.session,
            user_message
        )
