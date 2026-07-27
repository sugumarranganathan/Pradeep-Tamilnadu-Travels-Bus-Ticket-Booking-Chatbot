"""
Main Entry Point
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

from ui.app import demo

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        debug=True
    )
