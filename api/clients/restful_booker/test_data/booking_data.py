def get_booking_payload() -> dict:
    return {
        "firstname": "Autotester",
        "lastname": "Autotest",
        "totalprice": 228,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-03-30",
            "checkout": "2026-04-02"
        },
        "additionalneeds": "Breakfast"
    }

def get_updated_booking_payload() -> dict:
    return {
        "firstname": "UpdatedName",
        "lastname": "UpdatedLastName",
        "totalprice": 500,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-10-01",
            "checkout": "2025-10-15"
        },
        "additionalneeds": "Dinner"
    }