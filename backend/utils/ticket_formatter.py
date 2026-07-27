"""
Ticket Formatter
"""


def format_ticket(ticket):

    return f"""
========================================

🚌 Pradeep Tamilnadu Travels

BUS TICKET

========================================

Ticket No

{ticket["ticket_number"]}

Passenger

{ticket["passenger_name"]}

Mobile

{ticket["mobile"]}

Route

{ticket["route"]}

Bus

{ticket["bus_number"]}

Departure

{ticket["departure_time"]}

Seat

{ticket["seat"]}

Status

{ticket["status"]}

========================================
"""
