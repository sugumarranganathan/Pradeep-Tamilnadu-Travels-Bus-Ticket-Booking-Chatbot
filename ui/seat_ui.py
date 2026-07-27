import gradio as gr


def create_seat_buttons():

    seats = [
        ["A1", "A2"],
        ["A3", "A4"],
        ["B1", "B2"],
        ["B3", "B4"],
        ["C1", "C2"],
        ["C3", "C4"],
        ["D1", "D2"],
        ["D3", "D4"],
    ]

    with gr.Column():

        gr.Markdown("## 🚌 Select Your Seat")

        for row in seats:

            with gr.Row():

                for seat in row:

                    gr.Button(
                        value=seat,
                        size="sm"
                    )
