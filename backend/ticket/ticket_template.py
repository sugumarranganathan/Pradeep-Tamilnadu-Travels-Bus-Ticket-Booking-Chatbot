"""
Ticket Template
Pradeep Tamilnadu Travels
"""


class TicketTemplate:

    @staticmethod
    def get_ticket(ticket):

        return f"""
==================================================

🚌 PRADEEP TAMILNADU TRAVELS

BUS TICKET

==================================================

Ticket Number

{ticket["ticket_number"]}

Passenger

{ticket["passenger_name"]}

Mobile

{ticket["mobile"]}

Age

{ticket["age"]}

Gender

{ticket["gender"]}

--------------------------------------------------

Route

{ticket["route"]}

Bus Number

{ticket["bus_number"]}

Departure Time

{ticket["departure_time"]}

Journey Date

{ticket["journey_date"]}

Seat Number

{ticket["seat"]}

--------------------------------------------------

Booking Status

✅ CONFIRMED

==================================================
"""
