"""
Seat Layout
Pradeep Tamilnadu Travels
"""


class SeatLayout:

    def __init__(self):

        self.available_seats = [

            "A1", "A2", "A3", "A4",

            "B1", "B2", "B3", "B4",

            "C1", "C2", "C3", "C4",

            "D1", "D2", "D3", "D4"

        ]

    def get_layout(self):

        layout = """
🚌 Bus Seat Layout

Driver

A1   A2

A3   A4

----------------

B1   B2

B3   B4

----------------

C1   C2

C3   C4

----------------

D1   D2

D3   D4

Enter Seat Number
Example : B2
"""

        return layout

    def is_available(self, seat):

        return seat.upper() in self.available_seats

    def book(self, seat):

        seat = seat.upper()

        if seat in self.available_seats:

            self.available_seats.remove(seat)

            return True

        return False
