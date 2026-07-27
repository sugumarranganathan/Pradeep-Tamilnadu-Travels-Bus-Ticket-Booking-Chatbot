"""
Chatbot UI
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

from backend.conversation.conversation_manager import ConversationManager


# Create a single Conversation Manager instance
manager = ConversationManager()


def chatbot_reply(message, history):
    """
    Process user message and update chat history.
    """

    if history is None:
        history = []

    # Ignore empty messages
    if message is None or message.strip() == "":
        return "", history

    # Get chatbot response
    reply = manager.reply(message)

    # Update chat history
    history.append(
        (
            message,
            reply
        )
    )

    # Clear textbox and return updated history
    return "", history
