"""
Ticket Service
"""


def create_ticket(data):

    return {

        "ticket_number": data["ticket_number"],

        "passenger_name": data["passenger_name"],

        "route": data["route"],

        "bus_number": data["bus_number"],

        "seat_number": data["seat_number"],

        "journey_date": data["journey_date"],

        "departure_time": data["departure_time"],

        "fare": data["fare"],

        "status": "Confirmed"

    }
