from pydantic import BaseModel


class TicketResponse(BaseModel):

    ticket_number: str
    passenger_name: str
    route: str
    bus_number: str
    seat_number: str
    fare: int
