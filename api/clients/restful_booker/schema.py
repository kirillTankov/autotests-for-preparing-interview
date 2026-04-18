from datetime import date

from pydantic import BaseModel


class AuthData(BaseModel):
    username: str
    password: str


class BookingDates(BaseModel):
    checkin: date
    checkout: date


class BookingData(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None


class PartialBookingData(BaseModel):
    firstname: str | None = None
    lastname: str | None = None


class AuthResponse(BaseModel):
    token: str


class BookingResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None


class CreateBookingResponse(BaseModel):
    bookingid: int
    booking: BookingResponse


class BookingIdItem(BaseModel):
    bookingid: int