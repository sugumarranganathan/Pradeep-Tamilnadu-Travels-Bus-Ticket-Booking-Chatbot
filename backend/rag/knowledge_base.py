"""
Knowledge Base
Version : 1.0.0
"""

KNOWLEDGE_BASE = {

    "welcome":
    """
🚌 Welcome to Pradeep Tamilnadu Travels

Please select an option

1. Book Ticket
2. Bus Timings
3. Fare Details
4. Available Routes
5. Cancellation Policy
6. Customer Support
""",

    "routes":
    [
        "Chennai → Madurai",
        "Chennai → Coimbatore",
        "Chennai → Salem",
        "Chennai → Trichy"
    ],

    "timings":
    {
        "Chennai → Madurai":
        [
            "08:00 AM",
            "10:30 PM"
        ],

        "Chennai → Coimbatore":
        [
            "09:30 AM",
            "08:45 PM"
        ],

        "Chennai → Salem":
        [
            "07:00 AM",
            "10:00 PM"
        ],

        "Chennai → Trichy":
        [
            "06:30 AM",
            "09:00 PM"
        ]
    },

    "fare":
    {
        "Chennai → Madurai": "₹950",
        "Chennai → Coimbatore": "₹1100",
        "Chennai → Salem": "₹850",
        "Chennai → Trichy": "₹780"
    },

    "support":
    """
Customer Support

📞 +91 9876543210

📧 support@pradeeptravels.com
""",

    "cancellation":
    """
Cancellation Policy

• 24 Hours Before Journey : Full Refund

• 12 Hours Before Journey : 50% Refund

• Less Than 12 Hours : No Refund
"""
}
