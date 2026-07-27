from pydantic import BaseModel


class BookingRequest(BaseModel):

    passenger_name: str
    mobile: str
    route: str
    bus_number: str
    seat_number: str


class BookingResponse(BaseModel):

    ticket_number: str
    status: str
