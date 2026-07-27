from conversation.conversation_manager import ConversationManager

manager = ConversationManager()


def chatbot_reply(message, history):

    if history is None:
        history = []

    reply = manager.reply(message)

    history.append(
        (message, reply)
    )

    return "", history
