"""
Conversation Manager
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

from conversation.menu import WELCOME_MENU
from conversation.state_machine import ConversationState
from conversation.booking_flow import BookingFlow
from conversation.session_manager import SessionManager

from agents.ticket_agent import TicketAgent
from utils.ticket_formatter import format_ticket


class ConversationManager:

    def __init__(self):

        self.session = SessionManager()
        self.flow = BookingFlow()
        self.ticket_agent = TicketAgent()

    def reply(self, user_message):

        state = self.session.get_state()

        # ------------------------------------
        # Welcome Screen
        # ------------------------------------
        if state == ConversationState.WELCOME:

            self.session.set_state(
                ConversationState.MAIN_MENU
            )

            return WELCOME_MENU

        # ------------------------------------
        # Main Menu
        # ------------------------------------
        if state == ConversationState.MAIN_MENU:

            if user_message == "1":

                self.session.set_state(
                    ConversationState.ROUTE_SELECTION
                )

                return """
🚌 Select Route

1. Chennai → Madurai

2. Chennai → Coimbatore

3. Chennai → Salem

4. Chennai → Trichy
"""

            elif user_message == "2":

                return """
🕒 Bus Timings

1. Chennai → Madurai : 08:00 AM | 10:30 PM

2. Chennai → Coimbatore : 09:30 AM | 08:45 PM

3. Chennai → Salem : 07:00 AM | 10:00 PM

4. Chennai → Trichy : 06:30 AM | 09:00 PM
"""

            elif user_message == "3":

                return """
💰 Fare Details

Chennai → Madurai : ₹950

Chennai → Coimbatore : ₹1100

Chennai → Salem : ₹850

Chennai → Trichy : ₹780
"""

            elif user_message == "4":

                return """
🛣 Available Routes

• Chennai → Madurai

• Chennai → Coimbatore

• Chennai → Salem

• Chennai → Trichy
"""

            elif user_message == "5":

                return """
❌ Cancellation Policy

• Before 24 Hours : Full Refund

• Before 12 Hours : 50% Refund

• Less Than 12 Hours : No Refund
"""

            elif user_message == "6":

                return """
📞 Customer Support

Phone : +91 9876543210

Email : support@pradeeptravels.com
"""

            return "Please select a valid option (1-6)."

        # ------------------------------------
        # Booking Flow
        # ------------------------------------

        reply = self.flow.process(
            self.session,
            user_message
        )

        # ------------------------------------
        # Generate Ticket
        # ------------------------------------

        if self.session.get_state() == ConversationState.GENERATE_TICKET:

            booking = self.session.get_booking()

            ticket_data = self.ticket_agent.generate(
                booking
            )

            ticket = ticket_data["ticket"]

            image = ticket_data["image"]

            pdf = ticket_data["pdf"]

            ticket_text = format_ticket(ticket)

            self.session.set_state(
                ConversationState.COMPLETED
            )

            return f"""
✅ Booking Confirmed Successfully

{ticket_text}

----------------------------------------

🖼 Ticket Image

{image["image_name"]}

📄 Ticket PDF

{pdf["pdf_name"]}

Status : {pdf["status"]}

Thank you for choosing
Pradeep Tamilnadu Travels.
"""

        # ------------------------------------
        # Booking Completed
        # ------------------------------------

        if state == ConversationState.COMPLETED:

            if user_message.lower() in ["hi", "hello", "start"]:

                self.session = SessionManager()

                return WELCOME_MENU

            return """
✅ Your booking has already been completed.

Type

Hi

to start a new booking.
"""

        return reply
