"""
Gradio UI
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

import gradio as gr

from ui.theme import theme
from ui.components import APP_TITLE
from ui.chatbot_ui import chatbot_reply
from ui.seat_ui import create_seat_buttons


# -----------------------------
# Quick Menu Wrappers
# -----------------------------

def book_ticket(history):
    return chatbot_reply("1", history)


def bus_timings(history):
    return chatbot_reply("2", history)


def fare(history):
    return chatbot_reply("3", history)


def routes(history):
    return chatbot_reply("4", history)


def cancellation(history):
    return chatbot_reply("5", history)


def support(history):
    return chatbot_reply("6", history)


with gr.Blocks(
    title="Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot"
) as demo:

    gr.Markdown(APP_TITLE)
    chatbot = gr.Chatbot(
    label="🚌 Bus Ticket Booking Assistant",
    height=500
)
    
    with gr.Row():

        user_input = gr.Textbox(
            placeholder="Type your message...",
            label="Your Message",
            scale=8
        )

        send = gr.Button(
            "Send",
            scale=2
        )

    gr.Markdown("## 🚀 Quick Menu")

    with gr.Row():
        btn1 = gr.Button("🚌 Book Ticket")
        btn2 = gr.Button("🕒 Bus Timings")
        btn3 = gr.Button("💰 Fare")

    with gr.Row():
        btn4 = gr.Button("🛣 Routes")
        btn5 = gr.Button("❌ Cancellation")
        btn6 = gr.Button("📞 Support")

    with gr.Accordion("🪑 Seat Selection", open=False):
        create_seat_buttons()

    # -----------------------------
    # Chat
    # -----------------------------

    send.click(
        fn=chatbot_reply,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot]
    )

    user_input.submit(
        fn=chatbot_reply,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot]
    )

    # -----------------------------
    # Quick Menu
    # -----------------------------

    btn1.click(
        fn=book_ticket,
        inputs=[chatbot],
        outputs=[user_input, chatbot]
    )

    btn2.click(
        fn=bus_timings,
        inputs=[chatbot],
        outputs=[user_input, chatbot]
    )

    btn3.click(
        fn=fare,
        inputs=[chatbot],
        outputs=[user_input, chatbot]
    )

    btn4.click(
        fn=routes,
        inputs=[chatbot],
        outputs=[user_input, chatbot]
    )

    btn5.click(
        fn=cancellation,
        inputs=[chatbot],
        outputs=[user_input, chatbot]
    )

    btn6.click(
        fn=support,
        inputs=[chatbot],
        outputs=[user_input, chatbot]
    )


if __name__ == "__main__":
    demo.launch(
        share=True,
        theme=theme
    )
