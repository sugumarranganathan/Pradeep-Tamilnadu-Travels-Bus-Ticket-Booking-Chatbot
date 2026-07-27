import gradio as gr

from theme import theme
from components import APP_TITLE
from chatbot_ui import chatbot_reply
from seat_ui import create_seat_buttons


def menu_click(option, history):

    return chatbot_reply(option, history)


with gr.Blocks(
    theme=theme,
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
            scale=8
        )

        send = gr.Button(
            "Send",
            scale=2
        )

    gr.Markdown("### 🚀 Quick Menu")

    with gr.Row():

        btn1 = gr.Button("🚌 Book Ticket")
        btn2 = gr.Button("🕒 Bus Timings")
        btn3 = gr.Button("💰 Fare")

    with gr.Row():

        btn4 = gr.Button("🛣 Routes")
        btn5 = gr.Button("❌ Cancellation")
        btn6 = gr.Button("📞 Support")

    # ----------------------------------
    # Seat Selection
    # ----------------------------------

    with gr.Accordion("🪑 Seat Selection", open=False):

        create_seat_buttons()

    # ----------------------------------
    # Send Button
    # ----------------------------------

    send.click(
        chatbot_reply,
        inputs=[
            user_input,
            chatbot
        ],
        outputs=[
            user_input,
            chatbot
        ]
    )

    # ----------------------------------
    # Quick Menu Buttons
    # ----------------------------------

    btn1.click(
        menu_click,
        inputs=[
            "1",
            chatbot
        ],
        outputs=[
            user_input,
            chatbot
        ]
    )

    btn2.click(
        menu_click,
        inputs=[
            "2",
            chatbot
        ],
        outputs=[
            user_input,
            chatbot
        ]
    )

    btn3.click(
        menu_click,
        inputs=[
            "3",
            chatbot
        ],
        outputs=[
            user_input,
            chatbot
        ]
    )

    btn4.click(
        menu_click,
        inputs=[
            "4",
            chatbot
        ],
        outputs=[
            user_input,
            chatbot
        ]
    )

    btn5.click(
        menu_click,
        inputs=[
            "5",
            chatbot
        ],
        outputs=[
            user_input,
            chatbot
        ]
    )

    btn6.click(
        menu_click,
        inputs=[
            "6",
            chatbot
        ],
        outputs=[
            user_input,
            chatbot
        ]
    )


if __name__ == "__main__":
    demo.launch()
