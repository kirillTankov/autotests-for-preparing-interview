from api.clients.restful_booker.schema import BookingData, BookingDates, PartialBookingData


def get_booking_payload() -> BookingData:
    return BookingData(
        firstname="Autotester",
        lastname="Autotest",
        totalprice=228,
        depositpaid=True,
        bookingdates=BookingDates(
            checkin="2026-03-30",
            checkout="2026-04-02",
        ),
        additionalneeds="Breakfast",
    )


def get_updated_booking_payload() -> BookingData:
    return BookingData(
        firstname="UpdatedName",
        lastname="UpdatedLastName",
        totalprice=500,
        depositpaid=False,
        bookingdates=BookingDates(
            checkin="2025-10-01",
            checkout="2025-10-15",
        ),
        additionalneeds="Dinner",
    )


def get_partial_update_booking_payload() -> PartialBookingData:
    return PartialBookingData(
        firstname="PartialUpdateName",
        lastname="PartialUpdateLastName",
    )