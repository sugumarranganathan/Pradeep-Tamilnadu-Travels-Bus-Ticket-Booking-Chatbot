"""
Application Constants
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
"""

# ==========================================
# Company Information
# ==========================================

COMPANY_NAME = "Pradeep Tamilnadu Travels"

SUPPORT_PHONE = "+91 9876543210"

SUPPORT_EMAIL = "support@pradeeptravels.com"


# ==========================================
# Routes
# ==========================================

AVAILABLE_ROUTES = [
    "Chennai → Madurai",
    "Chennai → Coimbatore",
    "Chennai → Salem",
    "Chennai → Trichy"
]


# ==========================================
# Fare Details
# ==========================================

FARE_DETAILS = {
    "Chennai → Madurai": 950,
    "Chennai → Coimbatore": 1100,
    "Chennai → Salem": 850,
    "Chennai → Trichy": 780
}


# ==========================================
# Bus Timings
# ==========================================

BUS_TIMINGS = {
    "Chennai → Madurai": ["08:00 AM", "10:30 PM"],
    "Chennai → Coimbatore": ["09:30 AM", "08:45 PM"],
    "Chennai → Salem": ["07:00 AM", "10:00 PM"],
    "Chennai → Trichy": ["06:30 AM", "09:00 PM"]
}


# ==========================================
# Booking Options
# ==========================================

CONFIRM_BOOKING = "1"

CANCEL_BOOKING = "2"


# ==========================================
# Ticket
# ==========================================

TICKET_PREFIX = "PTT"

MAX_SEATS = 40


# ==========================================
# Cancellation Policy
# ==========================================

CANCELLATION_POLICY = {
    "24_hours": "Full Refund",
    "12_hours": "50% Refund",
    "less_than_12": "No Refund"
}
