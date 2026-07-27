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

    # Add user message
    history.append(
        {
            "role": "user",
            "content": message
        }
    )

    # Add assistant response
    history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    # Clear textbox and return updated history
    return "", history
