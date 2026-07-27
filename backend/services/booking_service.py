"""
Booking Service
"""

from database.sample_data import ROUTES, BUSES


def get_routes():

    return ROUTES


def get_buses(route):

    return [

        bus

        for bus in BUSES

        if bus["route"] == route

    ]


def generate_ticket_number():

    return "PT202600001"
