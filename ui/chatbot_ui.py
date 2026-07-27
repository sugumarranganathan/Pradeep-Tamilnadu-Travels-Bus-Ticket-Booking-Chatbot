"""
Chatbot UI
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

from backend.conversation.conversation_manager import ConversationManager

manager = ConversationManager()


def chatbot_reply(message, history):

    if history is None:
        history = []

    if message is None or message.strip() == "":
        return "", history

    reply = manager.reply(message)

    # Classic Gradio chat history
    history.append((message, reply))

    return "", history
