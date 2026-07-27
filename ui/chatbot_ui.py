"""
Chatbot UI
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

from backend.conversation.conversation_manager import ConversationManager

manager = ConversationManager()


def chatbot_reply(message, history):

    if history is None:
        history = []

    if not message or message.strip() == "":
        return "", history

    reply = manager.reply(message)

    history.append((message, reply))

    return "", history
